"""CLI output formatter for doc-check results."""

from typing import Optional
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from .base import OutputFormatter
from ..models import DocCheckResult


class CLIFormatter(OutputFormatter):
    """CLI output formatter that prints to console."""
    
    def __init__(self, output_dir: Optional[Path] = None, console: Optional[Console] = None):
        super().__init__(output_dir)
        self.console = console or Console()
    
    @property
    def default_filename(self) -> str:
        return "cli-output"  # Not used since we don't write to disk
    
    @property
    def file_extension(self) -> str:
        return ""  # Not used since we don't write to disk
    
    def write_results(self, result: DocCheckResult, filename: Optional[str] = None) -> Path:
        """Display results to console and return a dummy path."""
        self.display_results(result, verbose=True)
        return Path("console")  # Dummy path since we don't write to disk
    
    def display_results(self, result: DocCheckResult, verbose: bool = False) -> None:
        """Display the results in a formatted way."""
        
        # Summary panel
        summary_text = f"""
Total Questions: {result.total_questions}
Passed: [green]{result.passed_questions}[/green]
Failed: [red]{result.failed_questions}[/red]
Success Rate: {result.success_rate:.1f}%"""
        
        # Add timing information if available
        if result.duration_seconds:
            summary_text += f"\nDuration: {result.duration_seconds:.1f}s"
        
        # Add API usage information if available
        if result.api_usage:
            usage = result.api_usage
            summary_text += f"""
API Provider: {usage.provider}
Model: {usage.model}
API Calls: {usage.api_calls}
Total Tokens: {usage.total_tokens:,}
Input Tokens: {usage.input_tokens:,}
Output Tokens: {usage.output_tokens:,}
Estimated Cost: ${usage.estimated_cost:.4f}"""
        
        self.console.print(Panel(summary_text.strip(), title="Summary", border_style="blue"))
        
        # Results table
        table = Table(title="Question Results")
        table.add_column("Question", style="cyan", no_wrap=False)
        table.add_column("Status", justify="center")
        table.add_column("Evaluation", no_wrap=False)
        
        for question_result in result.results:
            status = "[green]PASS[/green]" if question_result.passed else "[red]FAIL[/red]"
            
            if question_result.error:
                evaluation = f"[red]Error: {question_result.error}[/red]"
            else:
                evaluation = question_result.evaluation_result
            
            table.add_row(
                question_result.name,
                status,
                evaluation
            )
        
        self.console.print(table)
        
        # Detailed output if verbose
        if verbose:
            self.console.print("\n[bold]Detailed Results:[/bold]")
            for i, question_result in enumerate(result.results, 1):
                self.console.print(f"\n[bold cyan]Question {i}: {question_result.name}[/bold cyan]")
                self.console.print(f"[dim]Q: {question_result.question}[/dim]")
                
                if question_result.error:
                    self.console.print(f"[red]Error: {question_result.error}[/red]")
                else:
                    self.console.print(f"[yellow]Answer:[/yellow] {question_result.answer}")
                    self.console.print(f"[blue]Evaluation:[/blue] {question_result.evaluation_result}")
    
    def display_debug_prompt(self, question: str, document_content: str, prompt_type: str) -> None:
        """Display debug information about the prompt being sent to the model."""
        # Import here to avoid circular imports
        if prompt_type == "question":
            from ..providers.openai import QUESTION_PROMPT_TEMPLATE
            prompt = QUESTION_PROMPT_TEMPLATE.format(
                question=question,
                document_content=document_content
            )
            title = "🔍 Debug: Question Prompt"
        else:
            prompt = f"Question: {question}\nDocument: {document_content}"
            title = "🔍 Debug: Prompt"
        
        # Truncate very long prompts for display
        if len(prompt) > 20000:
            prompt = prompt[:20000] + "\n\n... [truncated for display]"
        
        self.console.print(Panel(
            prompt,
            title=title,
            border_style="magenta",
            padding=(1, 2)
        ))
    
    def display_debug_evaluation(self, question: str, answer: str, evaluation_criteria: str) -> None:
        """Display debug information about the evaluation prompt being sent to the model."""
        # Import here to avoid circular imports
        from ..providers.openai import EVALUATION_PROMPT_TEMPLATE
        
        prompt = EVALUATION_PROMPT_TEMPLATE.format(
            question=question,
            answer=answer,
            evaluation_criteria=evaluation_criteria
        )
        
        # Truncate very long prompts for display
        if len(prompt) > 20000:
            prompt = prompt[:20000] + "\n\n... [truncated for display]"
        
        self.console.print(Panel(
            prompt,
            title="🔍 Debug: Evaluation Prompt",
            border_style="magenta",
            padding=(1, 2)
        ))
    
    def display_debug_raw_response(self, raw_response: str, response_type: str) -> None:
        """Display debug information about the raw model response."""
        # Truncate very long responses for display
        display_response = raw_response
        if len(raw_response) > 20000:
            display_response = raw_response[:20000] + "\n\n... [truncated for display]"
        
        self.console.print(Panel(
            display_response,
            title=f"🤖 Debug: Raw {response_type}",
            border_style="bright_blue",
            padding=(1, 2)
        ))
