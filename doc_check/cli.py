"""CLI interface for doc-check."""

import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from .core import DocumentChecker, detect_provider_from_model
from .models import DocCheckResult

# Default models
DEFAULT_OPENAI_MODEL = "gpt-4.1"
DEFAULT_ANTHROPIC_MODEL = "claude-sonnet-4-20250514"
DEFAULT_SUMMARIZER_MODEL = "claude-sonnet-4-20250514"


@click.group()
def cli():
    """Doc-check: CLI tool for checking documentation with LLM-based Q&A evaluation."""
    pass


@cli.command()
@click.argument('config_file', type=click.Path(exists=True, path_type=Path))
@click.option('--api-key', help='API key (or set OPENAI_API_KEY/ANTHROPIC_API_KEY env var)')
@click.option('--model', help='Model to use. OpenAI: gpt-4.1, gpt-4.1-mini, gpt-4.1-nano, gpt-4o, gpt-4o-mini, gpt-4.5-preview. Anthropic: claude-sonnet-4-20250514, claude-3-5-sonnet-20241022, claude-3-sonnet-20240229, claude-3-haiku-20240307. Default: gpt-4.1 for OpenAI, claude-sonnet-4-20250514 for Anthropic')
@click.option('--provider', type=click.Choice(['openai', 'anthropic']), default='openai', help='API provider to use (default: openai)')
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
@click.option('--verbose-dialog', is_flag=True, help='Show questions and answers in real-time as they are processed')
@click.option('--output', '-o', type=click.Path(path_type=Path), help='Save results to file (JSON/YAML based on extension)')
@click.option('--format', type=click.Choice(['json', 'yaml', 'auto']), default='auto', help='Output format (auto-detects from file extension)')
@click.option('--summarize', type=click.Choice(['minimal', 'light', 'medium', 'aggressive']), help='Summarize the document before asking questions. minimal: preserve nearly all content, light: preserve most details, medium: balanced summary, aggressive: high-level overview only')
@click.option('--summarizer-model', help='Model to use for document summarization (default: claude-sonnet-4-20250514)')
@click.option('--output-format', type=click.Choice(['html', 'junit']), help='Additional output format (html or junit)')
@click.option('--output-dir', type=click.Path(path_type=Path), help='Directory for additional output files (default: current directory)')
def check(
    config_file: Path,
    api_key: Optional[str],
    model: Optional[str],
    provider: str,
    verbose: bool,
    output: Optional[Path],
    format: str,
    summarize: Optional[str],
    summarizer_model: Optional[str],
    verbose_dialog: bool,
    output_format: Optional[str],
    output_dir: Optional[Path]
) -> None:
    """Check documentation using LLM-based Q&A evaluation.
    
    CONFIG_FILE: Path to the doc-check.yaml configuration file.
    """
    console = Console()
    
    try:
        # Set default model if not specified
        if model is None:
            model = DEFAULT_ANTHROPIC_MODEL if provider == "anthropic" else DEFAULT_OPENAI_MODEL
        
        # Auto-detect provider from model if not explicitly set to non-default
        # We check if provider is still the default 'openai' and if the model suggests otherwise
        if provider == "openai":  # This is the default value
            detected_provider = detect_provider_from_model(model)
            if detected_provider != "openai":
                provider = detected_provider
                console.print(f"[dim]Auto-detected provider '{provider}' from model '{model}'[/dim]")
        
        # Set default summarizer model if not specified
        if summarize and summarizer_model is None:
            summarizer_model = DEFAULT_SUMMARIZER_MODEL
        
        # Initialize checker
        checker = DocumentChecker(
            api_key=api_key, 
            model=model, 
            provider=provider,
            summarize=summarize,
            summarizer_model=summarizer_model,
            verbose_dialog=verbose_dialog
        )
        
        # Run the check
        console.print(f"[bold blue]Starting document check with config: {config_file}[/bold blue]")
        result = checker.check_document(config_file)
        
        # Display results
        display_results(console, result, verbose)
        
        # Save to file if requested
        if output:
            save_results(result, output, format)
            console.print(f"[green]Results saved to {output}[/green]")
        
        # Save additional output format if requested
        if output_format:
            from .output import get_formatter
            formatter_class = get_formatter(output_format)
            formatter = formatter_class(output_dir)
            output_path = formatter.write_results(result)
            console.print(f"[green]{output_format.upper()} results saved to {output_path}[/green]")
        
        # Print final summary
        console.print("\n" + "="*50)
        if result.failed_questions > 0:
            console.print(f"[red]✗ {result.failed_questions} question(s) failed out of {result.total_questions}[/red]")
            console.print(f"[dim]Success rate: {result.success_rate:.1f}%[/dim]")
            sys.exit(1)
        else:
            console.print(f"[green]✓ All {result.passed_questions} questions passed![/green]")
            console.print(f"[dim]Success rate: {result.success_rate:.1f}%[/dim]")
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


def save_results(result: DocCheckResult, output_path: Path, format: str = 'auto') -> None:
    """Save results to a file in the specified format."""
    import json
    import yaml
    
    # Auto-detect format from file extension
    if format == 'auto':
        suffix = output_path.suffix.lower()
        if suffix in ['.yaml', '.yml']:
            format = 'yaml'
        else:
            format = 'json'
    
    data = result.model_dump()
    
    with open(output_path, 'w', encoding='utf-8') as f:
        if format == 'yaml':
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, indent=2)
        else:
            json.dump(data, f, indent=2, ensure_ascii=False)


@cli.command()
@click.argument('config_file', type=click.Path(exists=True, path_type=Path))
def validate(config_file: Path) -> None:
    """Validate a configuration file without running checks."""
    console = Console()
    
    try:
        checker = DocumentChecker()
        config = checker.load_config(config_file)
        
        console.print(f"[green]✓ Configuration is valid[/green]")
        console.print(f"Document: {config.file}")
        console.print(f"Questions: {len(config.questions)}")
        
        for i, question in enumerate(config.questions, 1):
            console.print(f"  {i}. {question.name}")
            
    except Exception as e:
        console.print(f"[red]✗ Configuration validation failed: {e}[/red]")
        sys.exit(1)


# For backwards compatibility, make the main command the default
@click.command()
@click.argument('config_file', type=click.Path(exists=True, path_type=Path))
@click.option('--api-key', help='API key (or set OPENAI_API_KEY/ANTHROPIC_API_KEY env var)')
@click.option('--model', help='Model to use. OpenAI: gpt-4.1, gpt-4.1-mini, gpt-4.1-nano, gpt-4o, gpt-4o-mini, gpt-4.5-preview. Anthropic: claude-sonnet-4-20250514, claude-3-5-sonnet-20241022, claude-3-sonnet-20240229, claude-3-haiku-20240307. Default: gpt-4.1 for OpenAI, claude-sonnet-4-20250514 for Anthropic')
@click.option('--provider', type=click.Choice(['openai', 'anthropic']), default='openai', help='API provider to use (default: openai)')
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
@click.option('--verbose-dialog', is_flag=True, help='Show questions and answers in real-time as they are processed')
@click.option('--output', '-o', type=click.Path(path_type=Path), help='Save results to file (JSON/YAML based on extension)')
@click.option('--format', type=click.Choice(['json', 'yaml', 'auto']), default='auto', help='Output format (auto-detects from file extension)')
@click.option('--summarize', type=click.Choice(['minimal', 'light', 'medium', 'aggressive']), help='Summarize the document before asking questions. minimal: preserve nearly all content, light: preserve most details, medium: balanced summary, aggressive: high-level overview only')
@click.option('--summarizer-model', help='Model to use for document summarization (default: claude-sonnet-4-20250514)')
@click.option('--output-format', type=click.Choice(['html', 'junit']), help='Additional output format (html or junit)')
@click.option('--output-dir', type=click.Path(path_type=Path), help='Directory for additional output files (default: current directory)')
def main(
    config_file: Path,
    api_key: Optional[str],
    model: Optional[str],
    provider: str,
    verbose: bool,
    output: Optional[Path],
    format: str,
    summarize: Optional[str],
    summarizer_model: Optional[str],
    verbose_dialog: bool,
    output_format: Optional[str],
    output_dir: Optional[Path]
) -> None:
    """Check documentation using LLM-based Q&A evaluation.
    
    CONFIG_FILE: Path to the doc-check.yaml configuration file.
    """
    # Apply the same auto-detection logic for the main function
    console = Console()
    
    # Set default model if not specified
    if model is None:
        model = DEFAULT_ANTHROPIC_MODEL if provider == "anthropic" else DEFAULT_OPENAI_MODEL
    
    # Auto-detect provider from model if not explicitly set to non-default
    if provider == "openai":  # This is the default value
        detected_provider = detect_provider_from_model(model)
        if detected_provider != "openai":
            provider = detected_provider
            console.print(f"[dim]Auto-detected provider '{provider}' from model '{model}'[/dim]")
    
    return check(config_file, api_key, model, provider, verbose, output, format, summarize, summarizer_model, verbose_dialog, output_format, output_dir)


if __name__ == '__main__':
    main()
