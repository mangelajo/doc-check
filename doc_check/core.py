"""Core functionality for document checking."""

import os
import re
from pathlib import Path
from typing import Optional, Literal
from urllib.parse import urlparse
from urllib.request import urlopen
from datetime import datetime

import yaml
from openai import OpenAI
import anthropic
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn

from .models import DocCheckConfig, DocCheckResult, QuestionResult, ApiUsage
from .constants import (
    QUESTION_ANSWERING_SYSTEM_PROMPT,
    EVALUATION_SYSTEM_PROMPT,
    SUMMARIZATION_SYSTEM_PROMPT,
    QUESTION_PROMPT_TEMPLATE,
    EVALUATION_PROMPT_TEMPLATE,
    SUMMARIZATION_PROMPTS,
    DEFAULT_OPENAI_MODEL,
    DEFAULT_ANTHROPIC_MODEL,
    DEFAULT_SUMMARIZER_MODEL,
    OPENAI_MAX_TOKENS,
    ANTHROPIC_MAX_TOKENS,
    ANTHROPIC_SUMMARIZER_MAX_TOKENS,
    DEFAULT_TEMPERATURE,
    OPENAI_PRICING,
    ANTHROPIC_PRICING,
)


def detect_provider_from_model(model: str) -> str:
    """Detect the API provider based on the model name.
    
    Args:
        model: The model name to check
        
    Returns:
        The detected provider ('openai' or 'anthropic')
    """
    model_lower = model.lower()
    
    # Anthropic models
    if any(pattern in model_lower for pattern in ['claude', 'sonnet', 'haiku', 'opus']):
        return 'anthropic'
    
    # OpenAI models
    if any(pattern in model_lower for pattern in ['gpt', 'davinci', 'curie', 'babbage', 'ada']):
        return 'openai'
    
    # Default to openai for unknown models
    return 'openai'


class DocumentChecker:
    """Main class for checking documents with LLM evaluation."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = DEFAULT_OPENAI_MODEL, provider: Literal["openai", "anthropic"] = "openai", summarize: Optional[str] = None, summarizer_model: Optional[str] = None):
        """Initialize the document checker.
        
        Args:
            api_key: API key for the chosen provider. If None, will try to get from environment.
            model: Model to use for evaluation.
            provider: Which API provider to use ("openai" or "anthropic").
            summarize: Level of summarization to apply ('light', 'medium', 'aggressive', or None).
            summarizer_model: Model to use for document summarization.
        """
        self.provider = provider
        self.model = model
        self.summarize = summarize
        self.summarizer_model = summarizer_model or DEFAULT_SUMMARIZER_MODEL
        self.console = Console()
        self.api_usage = ApiUsage(provider=provider, model=model)
        
        if provider == "anthropic":
            self.anthropic_client = anthropic.Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))
            self.openai_client = None
            # Set default Claude model if using default OpenAI model
            if model == DEFAULT_OPENAI_MODEL:
                self.model = DEFAULT_ANTHROPIC_MODEL
                self.api_usage.model = self.model
        else:
            self.openai_client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
            self.anthropic_client = None
    
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
        if self.provider == "anthropic":
            return self._ask_question_anthropic(document_content, question)
        else:
            return self._ask_question_openai(document_content, question)
    
    def _ask_question_openai(self, document_content: str, question: str) -> str:
        """Ask a question using OpenAI API."""
        prompt = QUESTION_PROMPT_TEMPLATE.format(
            question=question,
            document_content=document_content
        )

        try:
            response = self.openai_client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": QUESTION_ANSWERING_SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                temperature=DEFAULT_TEMPERATURE
            )
            
            # Track usage
            if response.usage:
                self.api_usage.input_tokens += response.usage.prompt_tokens
                self.api_usage.output_tokens += response.usage.completion_tokens
                self.api_usage.total_tokens += response.usage.total_tokens
                self.api_usage.api_calls += 1
                self.api_usage.estimated_cost += self._calculate_openai_cost(response.usage)
            
            return response.choices[0].message.content or ""
        except Exception as e:
            raise RuntimeError(f"Failed to get answer from OpenAI: {e}")
    
    def _ask_question_anthropic(self, document_content: str, question: str) -> str:
        """Ask a question using Anthropic API."""
        prompt = QUESTION_PROMPT_TEMPLATE.format(
            question=question,
            document_content=document_content
        )

        try:
            response = self.anthropic_client.messages.create(
                model=self.model,
                max_tokens=ANTHROPIC_MAX_TOKENS,
                temperature=DEFAULT_TEMPERATURE,
                system=QUESTION_ANSWERING_SYSTEM_PROMPT,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            # Track usage
            if response.usage:
                self.api_usage.input_tokens += response.usage.input_tokens
                self.api_usage.output_tokens += response.usage.output_tokens
                self.api_usage.total_tokens += response.usage.input_tokens + response.usage.output_tokens
                self.api_usage.api_calls += 1
                self.api_usage.estimated_cost += self._calculate_anthropic_cost(response.usage)
            
            return response.content[0].text
        except Exception as e:
            raise RuntimeError(f"Failed to get answer from Anthropic: {e}")
    
    def evaluate_answer(self, question: str, answer: str, evaluation_criteria: str) -> tuple[bool, str]:
        """Evaluate an answer against criteria using LLM."""
        if self.provider == "anthropic":
            return self._evaluate_answer_anthropic(question, answer, evaluation_criteria)
        else:
            return self._evaluate_answer_openai(question, answer, evaluation_criteria)
    
    def _evaluate_answer_openai(self, question: str, answer: str, evaluation_criteria: str) -> tuple[bool, str]:
        """Evaluate an answer using OpenAI API."""
        prompt = EVALUATION_PROMPT_TEMPLATE.format(
            question=question,
            answer=answer,
            evaluation_criteria=evaluation_criteria
        )

        try:
            response = self.openai_client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": EVALUATION_SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                temperature=DEFAULT_TEMPERATURE
            )
            
            # Track usage
            if response.usage:
                self.api_usage.input_tokens += response.usage.prompt_tokens
                self.api_usage.output_tokens += response.usage.completion_tokens
                self.api_usage.total_tokens += response.usage.total_tokens
                self.api_usage.api_calls += 1
                self.api_usage.estimated_cost += self._calculate_openai_cost(response.usage)
            
            evaluation_text = response.choices[0].message.content or ""
            return self._parse_evaluation_result(evaluation_text)
            
        except Exception as e:
            raise RuntimeError(f"Failed to evaluate answer with OpenAI: {e}")
    
    def _evaluate_answer_anthropic(self, question: str, answer: str, evaluation_criteria: str) -> tuple[bool, str]:
        """Evaluate an answer using Anthropic API."""
        prompt = EVALUATION_PROMPT_TEMPLATE.format(
            question=question,
            answer=answer,
            evaluation_criteria=evaluation_criteria
        )

        try:
            response = self.anthropic_client.messages.create(
                model=self.model,
                max_tokens=2000,
                temperature=DEFAULT_TEMPERATURE,
                system=EVALUATION_SYSTEM_PROMPT,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            # Track usage
            if response.usage:
                self.api_usage.input_tokens += response.usage.input_tokens
                self.api_usage.output_tokens += response.usage.output_tokens
                self.api_usage.total_tokens += response.usage.input_tokens + response.usage.output_tokens
                self.api_usage.api_calls += 1
                self.api_usage.estimated_cost += self._calculate_anthropic_cost(response.usage)
            
            evaluation_text = response.content[0].text
            return self._parse_evaluation_result(evaluation_text)
            
        except Exception as e:
            raise RuntimeError(f"Failed to evaluate answer with Anthropic: {e}")
    
    def _parse_evaluation_result(self, evaluation_text: str) -> tuple[bool, str]:
        """Parse the evaluation result from LLM response."""
        # Improved parsing with multiple strategies
        passed = False
        explanation = evaluation_text
        
        # Strategy 1: Look for structured format
        result_match = re.search(r'RESULT:\s*(PASS|FAIL)', evaluation_text, re.IGNORECASE)
        explanation_match = re.search(r'EXPLANATION:\s*(.+)', evaluation_text, re.IGNORECASE | re.DOTALL)
        
        if result_match:
            passed = result_match.group(1).upper() == 'PASS'
            if explanation_match:
                explanation = explanation_match.group(1).strip()
        else:
            # Strategy 2: Look for pass/fail patterns in text
            pass_indicators = ['PASS', 'passes', 'meets the criteria', 'satisfies', 'adequate', 'sufficient']
            fail_indicators = ['FAIL', 'fails', 'does not meet', 'insufficient', 'inadequate', 'missing']
            
            text_upper = evaluation_text.upper()
            pass_count = sum(1 for indicator in pass_indicators if indicator.upper() in text_upper)
            fail_count = sum(1 for indicator in fail_indicators if indicator.upper() in text_upper)
            
            # If we have clear indicators, use them
            if pass_count > fail_count:
                passed = True
            elif fail_count > pass_count:
                passed = False
            else:
                # Strategy 3: Look at the overall sentiment/tone
                positive_words = ['good', 'correct', 'accurate', 'comprehensive', 'detailed', 'complete']
                negative_words = ['poor', 'incorrect', 'inaccurate', 'incomplete', 'missing', 'lacks']
                
                positive_count = sum(1 for word in positive_words if word in text_upper)
                negative_count = sum(1 for word in negative_words if word in text_upper)
                
                passed = positive_count > negative_count
        
        return passed, explanation
    
    def _calculate_openai_cost(self, usage) -> float:
        """Calculate estimated cost for OpenAI API usage."""
        # Default to gpt-4 pricing if model not found
        model_pricing = OPENAI_PRICING.get(self.model, OPENAI_PRICING[DEFAULT_OPENAI_MODEL])
        
        input_cost = (usage.prompt_tokens / 1000) * model_pricing["input"]
        output_cost = (usage.completion_tokens / 1000) * model_pricing["output"]
        
        return input_cost + output_cost
    
    def _calculate_anthropic_cost(self, usage) -> float:
        """Calculate estimated cost for Anthropic API usage."""
        # Default to sonnet 4 pricing if model not found
        model_pricing = ANTHROPIC_PRICING.get(self.model, ANTHROPIC_PRICING[DEFAULT_ANTHROPIC_MODEL])
        
        input_cost = (usage.input_tokens / 1000) * model_pricing["input"]
        output_cost = (usage.output_tokens / 1000) * model_pricing["output"]
        
        return input_cost + output_cost
    
    def summarize_document(self, document_content: str) -> str:
        """Summarize the document content using the summarizer model."""
        # Detect provider for summarizer model
        summarizer_provider = detect_provider_from_model(self.summarizer_model)
        
        # Get summarization prompt based on level
        prompt_template = SUMMARIZATION_PROMPTS.get(self.summarize, SUMMARIZATION_PROMPTS["medium"])
        prompt = prompt_template.format(document_content=document_content)

        try:
            if summarizer_provider == "anthropic":
                # Initialize Anthropic client for summarization if needed
                if not hasattr(self, 'summarizer_anthropic_client'):
                    self.summarizer_anthropic_client = anthropic.Anthropic(
                        api_key=os.getenv("ANTHROPIC_API_KEY")
                    )
                
                response = self.summarizer_anthropic_client.messages.create(
                    model=self.summarizer_model,
                    max_tokens=ANTHROPIC_SUMMARIZER_MAX_TOKENS,
                    temperature=DEFAULT_TEMPERATURE,
                    system=SUMMARIZATION_SYSTEM_PROMPT,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                
                # Track usage for summarization
                if response.usage:
                    self.api_usage.input_tokens += response.usage.input_tokens
                    self.api_usage.output_tokens += response.usage.output_tokens
                    self.api_usage.total_tokens += response.usage.input_tokens + response.usage.output_tokens
                    self.api_usage.api_calls += 1
                    self.api_usage.estimated_cost += self._calculate_anthropic_cost(response.usage)
                
                summary = response.content[0].text
                
            else:
                # Initialize OpenAI client for summarization if needed
                if not hasattr(self, 'summarizer_openai_client'):
                    self.summarizer_openai_client = OpenAI(
                        api_key=os.getenv("OPENAI_API_KEY")
                    )
                
                response = self.summarizer_openai_client.chat.completions.create(
                    model=self.summarizer_model,
                    messages=[
                        {"role": "system", "content": SUMMARIZATION_SYSTEM_PROMPT},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=DEFAULT_TEMPERATURE
                )
                
                # Track usage for summarization
                if response.usage:
                    self.api_usage.input_tokens += response.usage.prompt_tokens
                    self.api_usage.output_tokens += response.usage.completion_tokens
                    self.api_usage.total_tokens += response.usage.total_tokens
                    self.api_usage.api_calls += 1
                    self.api_usage.estimated_cost += self._calculate_openai_cost(response.usage)
                
                summary = response.choices[0].message.content or ""
            
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
                    document_content = self.summarize_document(document_content)
                    
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
                    self.console.print(f"[blue]Asking:[/blue] {question_config.name}")
                    answer = self.ask_question(document_content, question_config.question)
                    
                    # Evaluate the answer
                    self.console.print(f"[yellow]Evaluating:[/yellow] {question_config.name}")
                    passed, evaluation_result = self.evaluate_answer(
                        question_config.question,
                        answer,
                        question_config.answerEvaluation
                    )
                    
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
