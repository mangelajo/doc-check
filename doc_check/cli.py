"""CLI interface for doc-check."""

import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from .core import DocumentChecker


@click.command()
@click.argument('config_file', type=click.Path(exists=True, path_type=Path))
@click.option('--api-key', help='OpenAI API key (or set OPENAI_API_KEY env var)')
@click.option('--model', default='gpt-4', help='OpenAI model to use (default: gpt-4)')
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
@click.option('--output', '-o', type=click.Path(path_type=Path), help='Save results to JSON file')
def main(
    config_file: Path,
    api_key: Optional[str],
    model: str,
    verbose: bool,
    output: Optional[Path]
) -> None:
    """Check documentation using LLM-based Q&A evaluation.
    
    CONFIG_FILE: Path to the doc-check.yaml configuration file.
    """
    console = Console()
    
    try:
        # Initialize checker
        checker = DocumentChecker(api_key=api_key, model=model)
        
        # Run the check
        console.print(f"[bold blue]Starting document check with config: {config_file}[/bold blue]")
        result = checker.check_document(config_file)
        
        # Display results
        display_results(console, result, verbose)
        
        # Save to file if requested
        if output:
            save_results(result, output)
            console.print(f"[green]Results saved to {output}[/green]")
        
        # Exit with appropriate code
        if result.failed_questions > 0:
            console.print(f"[red]✗ {result.failed_questions} question(s) failed[/red]")
            sys.exit(1)
        else:
            console.print(f"[green]✓ All {result.passed_questions} questions passed[/green]")
            sys.exit(0)
            
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)


def display_results(console: Console, result: DocCheckResult, verbose: bool) -> None:
    """Display the results in a formatted way."""
    
    # Summary panel
    summary_text = f"""
Total Questions: {result.total_questions}
Passed: [green]{result.passed_questions}[/green]
Failed: [red]{result.failed_questions}[/red]
Success Rate: {result.success_rate:.1f}%
"""
    
    console.print(Panel(summary_text.strip(), title="Summary", border_style="blue"))
    
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
    
    console.print(table)
    
    # Detailed output if verbose
    if verbose:
        console.print("\n[bold]Detailed Results:[/bold]")
        for i, question_result in enumerate(result.results, 1):
            console.print(f"\n[bold cyan]Question {i}: {question_result.name}[/bold cyan]")
            console.print(f"[dim]Q: {question_result.question}[/dim]")
            
            if question_result.error:
                console.print(f"[red]Error: {question_result.error}[/red]")
            else:
                console.print(f"[yellow]Answer:[/yellow] {question_result.answer}")
                console.print(f"[blue]Evaluation:[/blue] {question_result.evaluation_result}")


def save_results(result: DocCheckResult, output_path: Path) -> None:
    """Save results to a JSON file."""
    import json
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result.model_dump(), f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
