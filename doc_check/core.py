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
from .rag import RAGIndexer

# Summarization prompt templates
SUMMARIZATION_PROMPTS = {
    "light": """Please provide a minimal summary of the following document. The summary should:
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

Please provide a concise, high-level summary that captures the essential concepts and main points of this document.""",

    "minimal": """Please clean up the following document by:
1. Converting any HTML content to clean, readable markdown format
2. Removing unnecessary or redundant HTML tags while preserving content
3. Cleaning up excessive markdown formatting (like multiple consecutive headers, redundant emphasis)
4. Standardizing markdown syntax (consistent header styles, list formatting, etc.)
5. Removing empty lines that don't serve a structural purpose, but not in code snippets
6. Preserving ALL actual content, code examples, links, and essential formatting
7. Maintaining the document's structure and readability
8. Converting HTML tables to markdown tables where possible
9. Remove any unnecessary styling or formatting that does not affect the content

The goal is to make the document cleaner and more readable while preserving 100% of the actual information content
and code snippets formatting.

Document to clean up:
{document_content}

Please return the cleaned up version of this document with improved formatting but identical content."""
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
    
    def __init__(self, api_key: Optional[str] = None, model: str = DEFAULT_OPENAI_MODEL, provider: Literal["openai", "anthropic", "ollama"] = "openai", summarize: Optional[str] = None, summarizer_model: Optional[str] = None, verbose_dialog: bool = False, debug: bool = False, use_rag: bool = False, rag_chunk_size: int = 512, rag_chunk_overlap: int = 50, rag_top_k: int = 5, rag_fallback: bool = False):
        """Initialize the document checker.
        
        Args:
            api_key: API key for the chosen provider. If None, will try to get from environment.
            model: Model to use for evaluation.
            provider: Which API provider to use ("openai", "anthropic", or "ollama").
            summarize: Level of summarization to apply ('light', 'medium', 'aggressive', or None).
            summarizer_model: Model to use for document summarization.
            verbose_dialog: Whether to show questions and answers in real-time.
            debug: Whether to show detailed debug information including prompts.
            use_rag: Whether to use RAG for document retrieval.
            rag_chunk_size: Size of each document chunk for RAG indexing.
            rag_chunk_overlap: Overlap between chunks for RAG indexing.
            rag_top_k: Number of top relevant chunks to retrieve for each question.
            rag_fallback: Whether to retry with full document if RAG-based answer fails evaluation.
        """
        self.provider = provider
        self.model = model
        self.summarize = summarize
        self.summarizer_model = summarizer_model or DEFAULT_SUMMARIZER_MODEL
        self.verbose_dialog = verbose_dialog
        self.debug = debug
        self.use_rag = use_rag
        self.rag_chunk_size = rag_chunk_size
        self.rag_chunk_overlap = rag_chunk_overlap
        self.rag_top_k = rag_top_k
        self.rag_fallback = rag_fallback
        self.console = Console()
        self.rag_indexer = None
        
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
        if self.use_rag and self.rag_indexer:
            # Use RAG to get relevant context
            context = self.rag_indexer.get_context_for_question(question)
            content_to_use = context
        else:
            content_to_use = document_content
        
        # Show debug information if requested
        if self.debug:
            from .output.cli import CLIFormatter
            formatter = CLIFormatter(console=self.console)
            formatter.display_debug_prompt(question, content_to_use, "question")
        
        answer = self.main_provider.ask(content_to_use, question)
        
        # Show raw response in debug mode
        if self.debug and hasattr(self.main_provider, 'last_raw_response'):
            from .output.cli import CLIFormatter
            formatter = CLIFormatter(console=self.console)
            formatter.display_debug_raw_response(self.main_provider.last_raw_response, "Question Response")
        
        return answer
    
    
    def evaluate_answer(self, question: str, answer: str, evaluation_criteria: str) -> tuple[bool, str]:
        """Evaluate an answer against criteria using LLM."""
        # Show debug information if requested
        if self.debug:
            from .output.cli import CLIFormatter
            formatter = CLIFormatter(console=self.console)
            formatter.display_debug_evaluation(question, answer, evaluation_criteria)
        
        result = self.main_provider.evaluate(question, answer, evaluation_criteria)
        
        # Show raw response in debug mode
        if self.debug and hasattr(self.main_provider, 'last_raw_response'):
            from .output.cli import CLIFormatter
            formatter = CLIFormatter(console=self.console)
            formatter.display_debug_raw_response(self.main_provider.last_raw_response, "Evaluation Response")
        
        return result
    
    
    
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
    
    def _cleanup_document(self, document_content: str) -> str:
        """Clean up document by removing unnecessary HTML/markdown tags and converting HTML to markdown."""
        import re
        
        content = document_content
        
        # First, extract and preserve code blocks to protect them from whitespace cleanup
        code_blocks = []
        inline_code = []
        
        # Extract triple-backtick code blocks
        def preserve_code_block(match):
            code_blocks.append(match.group(0))
            return f"__CODE_BLOCK_{len(code_blocks)-1}__"
        
        content = re.sub(r'```.*?```', preserve_code_block, content, flags=re.DOTALL)
        
        # Extract inline code (single backticks)
        def preserve_inline_code(match):
            inline_code.append(match.group(0))
            return f"__INLINE_CODE_{len(inline_code)-1}__"
        
        content = re.sub(r'`[^`\n]+`', preserve_inline_code, content)
        
        # Remove HTML comments
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        
        # Remove script and style tags completely (including content)
        content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.IGNORECASE | re.DOTALL)
        
        # Remove meta tags, link tags, and other head elements
        content = re.sub(r'<meta[^>]*/?>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<link[^>]*/?>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<title[^>]*>.*?</title>', '', content, flags=re.IGNORECASE | re.DOTALL)
        
        # Convert common HTML elements to markdown
        # Headers
        content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<h5[^>]*>(.*?)</h5>', r'##### \1', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<h6[^>]*>(.*?)</h6>', r'###### \1', content, flags=re.IGNORECASE | re.DOTALL)
        
        # Bold and italic
        content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', content, flags=re.IGNORECASE | re.DOTALL)
        
        # Code blocks and inline code (HTML to markdown conversion)
        content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'```\n\1\n```', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```', content, flags=re.IGNORECASE | re.DOTALL)
        
        # Links
        content = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.IGNORECASE | re.DOTALL)
        
        # Images
        content = re.sub(r'<img[^>]*alt=["\']([^"\']*)["\'][^>]*src=["\']([^"\']*)["\'][^>]*/?>', r'![\1](\2)', content, flags=re.IGNORECASE)
        content = re.sub(r'<img[^>]*src=["\']([^"\']*)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*/?>', r'![\2](\1)', content, flags=re.IGNORECASE)
        content = re.sub(r'<img[^>]*src=["\']([^"\']*)["\'][^>]*/?>', r'![](\1)', content, flags=re.IGNORECASE)
        
        # Tables (basic conversion)
        content = re.sub(r'<table[^>]*>', '\n', content, flags=re.IGNORECASE)
        content = re.sub(r'</table>', '\n', content, flags=re.IGNORECASE)
        content = re.sub(r'<tr[^>]*>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'</tr>', '\n', content, flags=re.IGNORECASE)
        content = re.sub(r'<th[^>]*>(.*?)</th>', r'| \1 ', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<td[^>]*>(.*?)</td>', r'| \1 ', content, flags=re.IGNORECASE | re.DOTALL)
        
        # Lists
        content = re.sub(r'<ul[^>]*>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'</ul>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<ol[^>]*>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'</ol>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', content, flags=re.IGNORECASE | re.DOTALL)
        
        # Paragraphs and line breaks
        content = re.sub(r'<p[^>]*>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'</p>', '\n\n', content, flags=re.IGNORECASE)
        content = re.sub(r'<br[^>]*/?>', '\n', content, flags=re.IGNORECASE)
        
        # Remove all remaining HTML tags (aggressive cleanup)
        content = re.sub(r'<[^>]+>', '', content)
        
        # Decode HTML entities
        import html
        content = html.unescape(content)
        
        # Clean up excessive whitespace and empty lines (but avoid code block placeholders)
        content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)  # Multiple empty lines to double
        content = re.sub(r'[ \t]+\n', '\n', content)  # Trailing whitespace
        content = re.sub(r'\n[ \t]+', '\n', content)  # Leading whitespace on lines
        content = re.sub(r'[ \t]+', ' ', content)  # Multiple spaces/tabs to single space
        
        # Clean up markdown formatting issues
        content = re.sub(r'#{7,}', '######', content)  # Too many header levels
        content = re.sub(r'\*{3,}', '**', content)  # Too many asterisks for bold
        content = re.sub(r'_{3,}', '__', content)  # Too many underscores
        
        # Remove excessive punctuation
        content = re.sub(r'\.{4,}', '...', content)  # Multiple dots to ellipsis
        content = re.sub(r'!{2,}', '!', content)  # Multiple exclamation marks
        content = re.sub(r'\?{2,}', '?', content)  # Multiple question marks
        
        # Clean up table formatting
        content = re.sub(r'\|\s*\|', '|', content)  # Empty table cells
        content = re.sub(r'\|\s*\n', '|\n', content)  # Trailing spaces in table rows
        
        # Remove standalone punctuation lines
        content = re.sub(r'\n[-=_*]{1,3}\n', '\n', content)
        
        # Clean up list formatting
        content = re.sub(r'\n-\s*\n', '\n', content)  # Empty list items
        content = re.sub(r'^-\s*$', '', content, flags=re.MULTILINE)  # Empty list items at line start
        
        # Restore code blocks and inline code with original formatting preserved
        for i, code_block in enumerate(code_blocks):
            content = content.replace(f"__CODE_BLOCK_{i}__", code_block)
        
        for i, inline in enumerate(inline_code):
            content = content.replace(f"__INLINE_CODE_{i}__", inline)
        
        return content.strip()
    
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
        
        # Handle cleanup mode without using LLM
        if self.summarize == "cleanup":
            try:
                summary = self._cleanup_document(document_content)
                # Save summary to cache
                self._save_cached_summary(cache_path, summary)
                return summary
            except Exception as e:
                raise RuntimeError(f"Failed to clean up document: {e}")
        

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
        
        # Index document for RAG if requested
        if self.use_rag:
            try:
                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    console=self.console
                ) as progress:
                    index_task = progress.add_task("Indexing document for RAG...", total=None)
                    self.rag_indexer = RAGIndexer(
                        chunk_size=self.rag_chunk_size,
                        chunk_overlap=self.rag_chunk_overlap
                    )
                    self.rag_indexer.index_document(document_content, doc_path)
                    
                self.console.print(f"[green]Document indexed successfully for RAG[/green] ({len(self.rag_indexer.chunks)} chunks created)")
            except Exception as e:
                self.console.print(f"[red]Error indexing document for RAG: {e}[/red]")
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
                    
                    # If RAG was used and the answer failed, try with full document if fallback is enabled
                    if self.use_rag and self.rag_fallback and not passed:
                        self.console.print(f"[yellow]RAG answer failed, retrying with full document...[/yellow]")
                        
                        # Ask the question again with full document
                        fallback_answer = self.main_provider.ask(document_content, question_config.question)
                        
                        if self.verbose_dialog:
                            self.console.print(Panel(
                                fallback_answer,
                                title="Fallback Answer (Full Document)",
                                border_style="blue",
                                padding=(1, 2)
                            ))
                        
                        # Evaluate the fallback answer with "(full document)" prefix
                        fallback_passed, fallback_evaluation = self.evaluate_answer(
                            question_config.question,
                            fallback_answer,
                            question_config.answerEvaluation
                        )
                        
                        # Prefix the evaluation result to indicate it used the full document
                        fallback_evaluation = f"(full document) {fallback_evaluation}"
                        
                        if self.verbose_dialog:
                            self.console.print(Panel(
                                fallback_evaluation,
                                title=f"Fallback Evaluation: {question_config.name}",
                                border_style="blue",
                                padding=(1, 2)
                            ))
                        
                        # Use the fallback result if it passed, otherwise keep the original
                        if fallback_passed:
                            answer = fallback_answer
                            evaluation_result = fallback_evaluation
                            passed = fallback_passed
                            self.console.print(f"[green]Fallback succeeded![/green]")
                        else:
                            self.console.print(f"[red]Fallback also failed[/red]")
                    
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
