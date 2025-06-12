"""Core functionality for document checking."""

import os
from pathlib import Path
from typing import Optional

import yaml
from openai import OpenAI
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

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
            return DocCheckConfig(**data)
        except Exception as e:
            raise ValueError(f"Failed to load config from {config_path}: {e}")
    
    def load_document(self, doc_path: Path) -> str:
        """Load document content from file."""
        try:
            with open(doc_path, 'r', encoding='utf-8') as f:
                return f.read()
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
            
            # Parse the result
            lines = evaluation_text.strip().split('\n')
            result_line = next((line for line in lines if line.startswith('RESULT:')), '')
            explanation_line = next((line for line in lines if line.startswith('EXPLANATION:')), '')
            
            if 'PASS' in result_line.upper():
                passed = True
            elif 'FAIL' in result_line.upper():
                passed = False
            else:
                # Fallback: look for pass/fail in the text
                passed = 'PASS' in evaluation_text.upper() and 'FAIL' not in evaluation_text.upper()
            
            explanation = explanation_line.replace('EXPLANATION:', '').strip() if explanation_line else evaluation_text
            
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
            console=self.console
        ) as progress:
            
            for i, question_config in enumerate(config.questions, 1):
                task = progress.add_task(
                    f"Processing question {i}/{len(config.questions)}: {question_config.name}",
                    total=None
                )
                
                try:
                    # Ask the question
                    progress.update(task, description=f"Asking question: {question_config.name}")
                    answer = self.ask_question(document_content, question_config.question)
                    
                    # Evaluate the answer
                    progress.update(task, description=f"Evaluating answer: {question_config.name}")
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
                    
                except Exception as e:
                    result = QuestionResult(
                        name=question_config.name,
                        question=question_config.question,
                        answer="",
                        evaluation_result="",
                        passed=False,
                        error=str(e)
                    )
                
                results.append(result)
                progress.remove_task(task)
        
        # Calculate summary
        passed_count = sum(1 for r in results if r.passed)
        failed_count = len(results) - passed_count
        
        return DocCheckResult(
            total_questions=len(results),
            passed_questions=passed_count,
            failed_questions=failed_count,
            results=results
        )
