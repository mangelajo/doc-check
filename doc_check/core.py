"""Core functionality for document checking."""

import os
import re
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse
from urllib.request import urlopen

import yaml
from openai import OpenAI
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn

from .models import DocCheckConfig, DocCheckResult, QuestionResult


class DocumentChecker:
    """Main class for checking documents with LLM evaluation."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        """Initialize the document checker.
        
        Args:
            api_key: OpenAI API key. If None, will try to get from environment.
            model: OpenAI model to use for evaluation.
        """
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.console = Console()
    
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
        prompt = f"""Based on the following document, please answer this question:

Question: {question}

Document:
{document_content}

Please provide a comprehensive answer based on the information in the document."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that answers questions about documentation accurately and comprehensively."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1
            )
            return response.choices[0].message.content or ""
        except Exception as e:
            raise RuntimeError(f"Failed to get answer from LLM: {e}")
    
    def evaluate_answer(self, question: str, answer: str, evaluation_criteria: str) -> tuple[bool, str]:
        """Evaluate an answer against criteria using LLM."""
        prompt = f"""Please evaluate the following answer against the given criteria.

Question: {question}

Answer: {answer}

Evaluation Criteria: {evaluation_criteria}

Please respond with:
1. PASS or FAIL
2. A brief explanation of your evaluation

Format your response as:
RESULT: [PASS/FAIL]
EXPLANATION: [Your explanation]"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert evaluator. Carefully assess whether the answer meets the specified criteria. Be strict but fair in your evaluation."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1
            )
            
            evaluation_text = response.choices[0].message.content or ""
            
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
            
        except Exception as e:
            raise RuntimeError(f"Failed to evaluate answer: {e}")
    
    def check_document(self, config_path: Path) -> DocCheckResult:
        """Check a document according to the configuration."""
        # Load configuration
        config = self.load_config(config_path)
        
        # Resolve document path relative to config file
        doc_path = config_path.parent / config.file
        document_content = self.load_document(doc_path)
        
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
        
        # Calculate summary
        passed_count = sum(1 for r in results if r.passed)
        failed_count = len(results) - passed_count
        
        return DocCheckResult(
            total_questions=len(results),
            passed_questions=passed_count,
            failed_questions=failed_count,
            results=results
        )
