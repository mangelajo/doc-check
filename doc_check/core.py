"""Core functionality for document checking."""

import os
import re
import hashlib
from pathlib import Path
from typing import Optional, Literal
from urllib.parse import urlparse
from urllib.request import urlopen
from datetime import datetime

import yaml
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn

from .models import DocCheckConfig, DocCheckResult, QuestionResult, ApiUsage
from .providers import OpenAIProvider, AnthropicProvider, OllamaProvider

# Summarization prompt templates
SUMMARIZATION_PROMPTS = {
    "minimal": """Please provide a minimal summary of the following document. The summary should:
1. Preserve nearly all key information, concepts, and details
2. Maintain the exact structure and organization of the original
3. Include all technical details, examples, and specifications
4. Be comprehensive enough to answer any detailed questions about the document's content
5. Preserve all code examples, configuration details, and specific instructions
6. Only remove redundant phrases and minor formatting - aim to reduce length by about 5-10% while keeping all essential content

Document to summarize:
{document_content}

Please provide a very detailed summary that retains virtually all essential information needed to answer questions about this document.""",

    "light": """Please provide a light summary of the following document. The summary should:
1. Preserve most key information, concepts, and details
2. Maintain the structure and organization of the original
3. Include all important technical details, examples, and specifications
4. Be comprehensive enough to answer detailed questions about the document's content
5. Preserve all code examples, configuration details, and specific instructions
6. Aim to reduce length by about 20-30% while keeping essential details

Document to summarize:
{document_content}

Please provide a detailed summary that retains nearly all essential information needed to answer questions about this document.""",

    "medium": """Please provide a balanced summary of the following document. The summary should:
1. Capture the most important information, concepts, and key details
2. Maintain the overall structure but condense sections appropriately
3. Include critical technical details and key examples
4. Be detailed enough to answer most questions about the document's content
5. Preserve essential code examples and important configuration details
6. Aim to reduce length by about 50% while keeping important information

Document to summarize:
{document_content}

Please provide a well-balanced summary that retains the important information needed to answer questions about this document.""",

    "aggressive": """Please provide a high-level summary of the following document. The summary should:
1. Focus on the main concepts, key points, and essential information only
2. Provide a condensed overview of the document's structure and purpose
3. Include only the most critical technical details and examples
4. Cover the core topics at a level sufficient for general understanding
5. Preserve only the most essential code examples or configuration details
6. Aim to reduce length by about 70-80% while keeping core concepts

Document to summarize:
{document_content}

Please provide a concise, high-level summary that captures the essential concepts and main points of this document."""
}

# Default models
DEFAULT_OPENAI_MODEL = "gpt-4.1"
DEFAULT_ANTHROPIC_MODEL = "claude-sonnet-4-20250514"
DEFAULT_OLLAMA_MODEL = "llama3.2"
DEFAULT_SUMMARIZER_MODEL = "claude-sonnet-4-20250514"



def detect_provider_from_model(model: str) -> str:
    """Detect the API provider based on the model name.
    
    Args:
        model: The model name to check
        
    Returns:
        The detected provider ('openai', 'anthropic', or 'ollama')
    """
    model_lower = model.lower()
    
    # Anthropic models
    if any(pattern in model_lower for pattern in ['claude', 'sonnet', 'haiku', 'opus']):
        return 'anthropic'
    
    # OpenAI models
    if any(pattern in model_lower for pattern in ['gpt', 'davinci', 'curie', 'babbage', 'ada']):
        return 'openai'
    
    # Ollama models (common local models)
    if any(pattern in model_lower for pattern in [
        'llama', 'mistral', 'mixtral', 'codellama', 'phi3', 'gemma', 
        'qwen', 'deepseek', 'neural-chat', 'starling', 'vicuna', 
        'orca-mini', 'wizard-vicuna', 'nous-hermes'
    ]):
        return 'ollama'
    
    # Default to openai for unknown models
    return 'openai'


class DocumentChecker:
    """Main class for checking documents with LLM evaluation."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = DEFAULT_OPENAI_MODEL, provider: Literal["openai", "anthropic", "ollama"] = "openai", summarize: Optional[str] = None, summarizer_model: Optional[str] = None, verbose_dialog: bool = False):
        """Initialize the document checker.
        
        Args:
            api_key: API key for the chosen provider. If None, will try to get from environment.
            model: Model to use for evaluation.
            provider: Which API provider to use ("openai", "anthropic", or "ollama").
            summarize: Level of summarization to apply ('light', 'medium', 'aggressive', or None).
            summarizer_model: Model to use for document summarization.
            verbose_dialog: Whether to show questions and answers in real-time.
        """
        self.provider = provider
        self.model = model
        self.summarize = summarize
        self.summarizer_model = summarizer_model or DEFAULT_SUMMARIZER_MODEL
        self.verbose_dialog = verbose_dialog
        self.console = Console()
        
        # Initialize the main provider
        if provider == "anthropic":
            # Set default Claude model if using default OpenAI model
            if model == DEFAULT_OPENAI_MODEL:
                self.model = DEFAULT_ANTHROPIC_MODEL
            self.main_provider = AnthropicProvider(api_key=api_key, model=self.model)
        elif provider == "ollama":
            # Set default Ollama model if using default OpenAI model
            if model == DEFAULT_OPENAI_MODEL:
                self.model = DEFAULT_OLLAMA_MODEL
            self.main_provider = OllamaProvider(model=self.model)
        else:
            self.main_provider = OpenAIProvider(api_key=api_key, model=self.model)
        
        # Initialize the summarizer provider (may be different from main provider)
        summarizer_provider_type = detect_provider_from_model(self.summarizer_model)
        if summarizer_provider_type == "anthropic":
            self.summarizer_provider = AnthropicProvider(api_key=api_key, model=self.summarizer_model)
        elif summarizer_provider_type == "ollama":
            self.summarizer_provider = OllamaProvider(model=self.summarizer_model)
        else:
            self.summarizer_provider = OpenAIProvider(api_key=api_key, model=self.summarizer_model)
        
        # Use the main provider's API usage for tracking
        self.api_usage = self.main_provider.api_usage
    
    def load_config(self, config_path: Path) -> DocCheckConfig:
        """Load configuration from YAML file."""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            # Validate required fields
            if not data:
                raise ValueError("Configuration file is empty")
            
            if 'file' not in data:
                raise ValueError("Configuration must specify 'file' field")
                
            if 'questions' not in data or not data['questions']:
                raise ValueError("Configuration must specify at least one question")
            
            config = DocCheckConfig(**data)
            
            # Validate questions
            for i, question in enumerate(config.questions):
                if not question.name.strip():
                    raise ValueError(f"Question {i+1} must have a non-empty name")
                if not question.question.strip():
                    raise ValueError(f"Question '{question.name}' must have a non-empty question")
                if not question.answerEvaluation.strip():
                    raise ValueError(f"Question '{question.name}' must have non-empty answerEvaluation")
            
            return config
        except Exception as e:
            raise ValueError(f"Failed to load config from {config_path}: {e}")
    
    def load_document(self, doc_path: Path) -> str:
        """Load document content from file or URL."""
        doc_str = str(doc_path)
        
        # Check if it's a URL
        if doc_str.startswith(('http://', 'https://')):
            try:
                with urlopen(doc_str) as response:
                    content = response.read()
                    # Try to decode as UTF-8, fallback to latin-1
                    try:
                        return content.decode('utf-8')
                    except UnicodeDecodeError:
                        return content.decode('latin-1')
            except Exception as e:
                raise ValueError(f"Failed to load document from URL {doc_str}: {e}")
        
        # Handle local file
        try:
            with open(doc_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Basic validation
            if not content.strip():
                raise ValueError(f"Document {doc_path} is empty")
                
            return content
        except FileNotFoundError:
            raise ValueError(f"Document file not found: {doc_path}")
        except Exception as e:
            raise ValueError(f"Failed to load document from {doc_path}: {e}")
    
    def ask_question(self, document_content: str, question: str) -> str:
        """Ask a question about the document using LLM."""
        return self.main_provider.ask(document_content, question)
    
    
    def evaluate_answer(self, question: str, answer: str, evaluation_criteria: str) -> tuple[bool, str]:
        """Evaluate an answer against criteria using LLM."""
        return self.main_provider.evaluate(question, answer, evaluation_criteria)
    
    
    
    def _get_document_hash(self, content: str) -> str:
        """Calculate SHA1 hash of document content."""
        return hashlib.sha1(content.encode('utf-8')).hexdigest()
    
    def _get_cache_filename(self, doc_path: Path, content_hash: str, level: str, model: str) -> Path:
        """Generate cache filename for summarized document."""
        # Clean model name for filename (replace problematic characters)
        clean_model = re.sub(r'[^\w\-.]', '_', model)
        cache_name = f"{doc_path.name}.{content_hash}.summary.{level}.{clean_model}"
        return doc_path.parent / cache_name
    
    def _load_cached_summary(self, cache_path: Path) -> Optional[str]:
        """Load cached summary if it exists."""
        if cache_path.exists():
            try:
                with open(cache_path, 'r', encoding='utf-8') as f:
                    return f.read()
            except Exception:
                # If we can't read the cache file, ignore it
                pass
        return None
    
    def _save_cached_summary(self, cache_path: Path, summary: str) -> None:
        """Save summary to cache file."""
        try:
            with open(cache_path, 'w', encoding='utf-8') as f:
                f.write(summary)
        except Exception:
            # If we can't write the cache file, just continue without caching
            pass
    
    def summarize_document(self, document_content: str, doc_path: Path) -> str:
        """Summarize the document content using the summarizer model."""
        # Calculate hash of document content for caching
        content_hash = self._get_document_hash(document_content)
        cache_path = self._get_cache_filename(doc_path, content_hash, self.summarize, self.summarizer_model)
        
        # Check for cached summary
        cached_summary = self._load_cached_summary(cache_path)
        if cached_summary:
            self.console.print(f"[green]Using cached summary[/green] ({cache_path.name})")
            return cached_summary
        
        # Detect provider for summarizer model
        summarizer_provider = detect_provider_from_model(self.summarizer_model)
        
        # Get summarization prompt based on level
        prompt_template = SUMMARIZATION_PROMPTS.get(self.summarize, SUMMARIZATION_PROMPTS["medium"])
        prompt = prompt_template.format(document_content=document_content)

        try:
            summary = self.summarizer_provider.summarize(prompt)
            
            # Merge summarizer usage into main API usage tracking
            self.api_usage.input_tokens += self.summarizer_provider.api_usage.input_tokens
            self.api_usage.output_tokens += self.summarizer_provider.api_usage.output_tokens
            self.api_usage.total_tokens += self.summarizer_provider.api_usage.total_tokens
            self.api_usage.api_calls += self.summarizer_provider.api_usage.api_calls
            self.api_usage.estimated_cost += self.summarizer_provider.api_usage.estimated_cost
            
            # Reset summarizer usage to avoid double counting
            self.summarizer_provider.api_usage = type(self.summarizer_provider.api_usage)(
                provider=self.summarizer_provider.api_usage.provider,
                model=self.summarizer_provider.api_usage.model
            )
            
            # Save summary to cache
            self._save_cached_summary(cache_path, summary)
            
            return summary
            
        except Exception as e:
            raise RuntimeError(f"Failed to summarize document: {e}")
    
    def check_document(self, config_path: Path) -> DocCheckResult:
        """Check a document according to the configuration."""
        start_time = datetime.now()
        
        # Load configuration
        config = self.load_config(config_path)
        
        # Resolve document path relative to config file
        doc_path = config_path.parent / config.file
        document_content = self.load_document(doc_path)
        
        # Summarize document if requested
        if self.summarize:
            try:
                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    console=self.console
                ) as progress:
                    summarize_task = progress.add_task(f"Summarizing document ({self.summarize} level)...", total=None)
                    original_length = len(document_content)
                    document_content = self.summarize_document(document_content, doc_path)
                    
                reduction_pct = ((original_length - len(document_content)) / original_length) * 100
                self.console.print(f"[green]Document summarized successfully ({self.summarize} level)[/green] (Original: {original_length:,} chars → Summary: {len(document_content):,} chars, {reduction_pct:.1f}% reduction)")
            except Exception as e:
                self.console.print(f"[red]Error: {e}[/red]")
                raise
        
        results = []
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            console=self.console
        ) as progress:
            
            main_task = progress.add_task(
                f"Processing {len(config.questions)} questions",
                total=len(config.questions)
            )
            
            for i, question_config in enumerate(config.questions, 1):
                progress.update(main_task, description=f"Question {i}/{len(config.questions)}: {question_config.name}")
                
                try:
                    # Ask the question
                    if self.verbose_dialog:
                        self.console.print(Panel(
                            question_config.question,
                            title=f"Asking: {question_config.name}",
                            border_style="cyan",
                            padding=(1, 2)
                        ))
                    else:
                        self.console.print(f"[cyan]Asking:[/cyan] {question_config.name}")
                    
                    answer = self.ask_question(document_content, question_config.question)
                    
                    if self.verbose_dialog:
                        self.console.print(Panel(
                            answer,
                            title="Answer",
                            border_style="green",
                            padding=(1, 2)
                        ))
                    
                    # Evaluate the answer
                    passed, evaluation_result = self.evaluate_answer(
                        question_config.question,
                        answer,
                        question_config.answerEvaluation
                    )
                    
                    if self.verbose_dialog:
                        self.console.print(Panel(
                            evaluation_result,
                            title=f"Evaluating: {question_config.name}",
                            border_style="yellow",
                            padding=(1, 2)
                        ))
                    else:
                        self.console.print(f"[yellow]Evaluating:[/yellow] {question_config.name}")
                    
                    result = QuestionResult(
                        name=question_config.name,
                        question=question_config.question,
                        answer=answer,
                        evaluation_result=evaluation_result,
                        passed=passed
                    )
                    
                    # Show immediate result
                    status = "[green]✓ PASS[/green]" if passed else "[red]✗ FAIL[/red]"
                    self.console.print(f"[dim]Result:[/dim] {status} - {question_config.name}")
                    
                except Exception as e:
                    self.console.print(f"[red]Error processing {question_config.name}: {e}[/red]")
                    result = QuestionResult(
                        name=question_config.name,
                        question=question_config.question,
                        answer="",
                        evaluation_result="",
                        passed=False,
                        error=str(e)
                    )
                
                results.append(result)
                progress.update(main_task, advance=1)
        
        end_time = datetime.now()
        
        # Calculate summary
        passed_count = sum(1 for r in results if r.passed)
        failed_count = len(results) - passed_count
        
        return DocCheckResult(
            total_questions=len(results),
            passed_questions=passed_count,
            failed_questions=failed_count,
            results=results,
            api_usage=self.api_usage,
            start_time=start_time,
            end_time=end_time,
            summarization_level=self.summarize
        )
