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
DEFAULT_OLLAMA_MODEL = "llama3.2"
DEFAULT_SUMMARIZER_MODEL = "claude-sonnet-4-20250514"


@click.group()
def cli():
    """Doc-check: CLI tool for checking documentation with LLM-based Q&A evaluation."""
    pass


@cli.command()
@click.argument('config_file', type=click.Path(exists=True, path_type=Path))
@click.option('--api-key', help='API key (or set OPENAI_API_KEY/ANTHROPIC_API_KEY env var)')
@click.option('--model', help='Model to use. OpenAI: gpt-4.1, gpt-4.1-mini, gpt-4.1-nano, gpt-4o, gpt-4o-mini, gpt-4.5-preview. Anthropic: claude-sonnet-4-20250514, claude-3-5-sonnet-20241022, claude-3-sonnet-20240229, claude-3-haiku-20240307. Ollama: llama3.2, llama3.1, mistral, mixtral, codellama, phi3, gemma. Default: gpt-4.1 for OpenAI, claude-sonnet-4-20250514 for Anthropic, llama3.2 for Ollama')
@click.option('--provider', type=click.Choice(['openai', 'anthropic', 'ollama']), default='openai', help='API provider to use (default: openai)')
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
@click.option('--verbose-dialog', is_flag=True, help='Show questions and answers in real-time as they are processed')
@click.option('--debug', is_flag=True, help='Show detailed debug information including prompts sent to the model')
@click.option('--output', '-o', type=click.Path(path_type=Path), help='Save results to file (JSON/YAML based on extension)')
@click.option('--format', type=click.Choice(['json', 'yaml', 'html', 'auto']), default='auto', help='Output format (auto-detects from file extension)')
@click.option('--summarize', type=click.Choice(['minimal', 'light', 'medium', 'aggressive', 'cleanup']), help='Summarize the document before asking questions. minimal: preserve nearly all content, light: preserve most details, medium: balanced summary, aggressive: high-level overview only, cleanup: remove unnecessary markdown/HTML tags and convert HTML to markdown')
@click.option('--summarizer-model', help='Model to use for document summarization (default: claude-sonnet-4-20250514)')
@click.option('--output-format', type=click.Choice(['html', 'junit']), help='Additional output format (html or junit)')
@click.option('--output-dir', type=click.Path(path_type=Path), help='Directory for additional output files (default: current directory)')
@click.option('--use-rag', is_flag=True, help='Use RAG (Retrieval-Augmented Generation) to provide only relevant document chunks to the model')
@click.option('--rag-chunk-size', type=int, default=512, help='Size of each document chunk for RAG indexing (default: 512)')
@click.option('--rag-chunk-overlap', type=int, default=50, help='Overlap between chunks for RAG indexing (default: 50)')
@click.option('--rag-top-k', type=int, default=5, help='Number of top relevant chunks to retrieve for each question (default: 5)')
@click.option('--rag-fallback', is_flag=True, help='Retry with full document if RAG-based answer fails evaluation')
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
    debug: bool,
    output_format: Optional[str],
    output_dir: Optional[Path],
    use_rag: bool,
    rag_chunk_size: int,
    rag_chunk_overlap: int,
    rag_top_k: int,
    rag_fallback: bool
) -> None:
    """Check documentation using LLM-based Q&A evaluation.
    
    CONFIG_FILE: Path to the doc-check.yaml configuration file.
    """
    console = Console()
    
    try:
        # Load configuration first to get defaults from config file
        temp_checker = DocumentChecker()
        config = temp_checker.load_config(config_file)
        
        # Use config file values as defaults if command-line options weren't specified
        # Provider: use config value if CLI is default and config specifies one
        if provider == "openai" and config.provider:  # CLI default is "openai"
            provider = config.provider
            console.print(f"[dim]Using provider '{provider}' from config file[/dim]")
        
        # Model: use config value if CLI didn't specify one
        if model is None and config.model:
            model = config.model
            console.print(f"[dim]Using model '{model}' from config file[/dim]")
        
        # API key: use config value if CLI didn't specify one
        if api_key is None and config.api_key:
            api_key = config.api_key
        
        # Summarize: use config value if CLI didn't specify one
        if summarize is None and config.summarize:
            summarize = config.summarize
            console.print(f"[dim]Using summarize '{summarize}' from config file[/dim]")
        
        # Summarizer model: use config value if CLI didn't specify one
        if summarizer_model is None and config.summarizer_model:
            summarizer_model = config.summarizer_model
        
        # RAG settings: use config values if CLI used defaults
        if not use_rag and config.use_rag:
            use_rag = config.use_rag
            console.print(f"[dim]Using RAG settings from config file[/dim]")
        
        if rag_chunk_size == 512 and config.rag_chunk_size:  # 512 is CLI default
            rag_chunk_size = config.rag_chunk_size
        
        if rag_chunk_overlap == 50 and config.rag_chunk_overlap:  # 50 is CLI default
            rag_chunk_overlap = config.rag_chunk_overlap
        
        if rag_top_k == 5 and config.rag_top_k:  # 5 is CLI default
            rag_top_k = config.rag_top_k
        
        if not rag_fallback and config.rag_fallback:
            rag_fallback = config.rag_fallback
        
        # Output settings: use config values if CLI didn't specify
        if output_format is None and config.output_format:
            output_format = config.output_format
        
        if output_dir is None and config.output_dir:
            output_dir = Path(config.output_dir)
        
        # Set default model if still not specified
        if model is None:
            if provider == "anthropic":
                model = DEFAULT_ANTHROPIC_MODEL
            elif provider == "ollama":
                model = DEFAULT_OLLAMA_MODEL
            else:
                model = DEFAULT_OPENAI_MODEL
        
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
            verbose_dialog=verbose_dialog,
            debug=debug,
            use_rag=use_rag,
            rag_chunk_size=rag_chunk_size,
            rag_chunk_overlap=rag_chunk_overlap,
            rag_top_k=rag_top_k,
            rag_fallback=rag_fallback
        )
        
        # Run the check
        console.print(f"[bold cyan]Starting document check with config: {config_file}[/bold cyan]")
        result = checker.check_document(config_file)
        
        # Display results
        display_results(console, result, verbose)
        
        # Save to file if requested
        if output:
            # Auto-detect format from file extension if format is 'auto'
            actual_format = format
            if format == 'auto':
                suffix = output.suffix.lower()
                if suffix == '.html':
                    actual_format = 'html'
                elif suffix in ['.yaml', '.yml']:
                    actual_format = 'yaml'
                else:
                    actual_format = 'json'
            
            if actual_format == 'html':
                from .output import get_formatter
                formatter_class = get_formatter('html')
                formatter = formatter_class(output.parent if output.parent != Path('.') else None)
                output_path = formatter.write_results(result, output.stem)
                console.print(f"[green]HTML results saved to {output_path}[/green]")
            else:
                save_results(result, output, actual_format)
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
    from .output import CLIFormatter
    
    formatter = CLIFormatter(console=console)
    formatter.display_results(result, verbose=verbose)


def save_results(result: DocCheckResult, output_path: Path, format: str = 'auto') -> None:
    """Save results to a file in the specified format."""
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
            # Use the custom JSON serialization method
            f.write(result.model_dump_json(indent=2))


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
@click.option('--model', help='Model to use. OpenAI: gpt-4.1, gpt-4.1-mini, gpt-4.1-nano, gpt-4o, gpt-4o-mini, gpt-4.5-preview. Anthropic: claude-sonnet-4-20250514, claude-3-5-sonnet-20241022, claude-3-sonnet-20240229, claude-3-haiku-20240307. Ollama: llama3.2, llama3.1, mistral, mixtral, codellama, phi3, gemma. Default: gpt-4.1 for OpenAI, claude-sonnet-4-20250514 for Anthropic, llama3.2 for Ollama')
@click.option('--provider', type=click.Choice(['openai', 'anthropic', 'ollama']), default='openai', help='API provider to use (default: openai)')
@click.option('--verbose', '-v', is_flag=True, help='Show detailed output')
@click.option('--verbose-dialog', is_flag=True, help='Show questions and answers in real-time as they are processed')
@click.option('--debug', is_flag=True, help='Show detailed debug information including prompts sent to the model')
@click.option('--output', '-o', type=click.Path(path_type=Path), help='Save results to file (JSON/YAML based on extension)')
@click.option('--format', type=click.Choice(['json', 'yaml', 'html', 'auto']), default='auto', help='Output format (auto-detects from file extension)')
@click.option('--summarize', type=click.Choice(['minimal', 'light', 'medium', 'aggressive', 'cleanup']), help='Summarize the document before asking questions. minimal: preserve nearly all content, light: preserve most details, medium: balanced summary, aggressive: high-level overview only, cleanup: remove unnecessary markdown/HTML tags and convert HTML to markdown')
@click.option('--summarizer-model', help='Model to use for document summarization (default: claude-sonnet-4-20250514)')
@click.option('--output-format', type=click.Choice(['html', 'junit']), help='Additional output format (html or junit)')
@click.option('--output-dir', type=click.Path(path_type=Path), help='Directory for additional output files (default: current directory)')
@click.option('--use-rag', is_flag=True, help='Use RAG (Retrieval-Augmented Generation) to provide only relevant document chunks to the model')
@click.option('--rag-chunk-size', type=int, default=512, help='Size of each document chunk for RAG indexing (default: 512)')
@click.option('--rag-chunk-overlap', type=int, default=50, help='Overlap between chunks for RAG indexing (default: 50)')
@click.option('--rag-top-k', type=int, default=5, help='Number of top relevant chunks to retrieve for each question (default: 5)')
@click.option('--rag-fallback', is_flag=True, help='Retry with full document if RAG-based answer fails evaluation')
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
    debug: bool,
    verbose_dialog: bool,
    output_format: Optional[str],
    output_dir: Optional[Path],
    use_rag: bool,
    rag_chunk_size: int,
    rag_chunk_overlap: int,
    rag_top_k: int,
    rag_fallback: bool
) -> None:
    """Check documentation using LLM-based Q&A evaluation.
    
    CONFIG_FILE: Path to the doc-check.yaml configuration file.
    """
    # The main function now just delegates to check() which handles config loading
    return check(config_file, api_key, model, provider, verbose, output, format, summarize, summarizer_model, verbose_dialog, debug, output_format, output_dir, use_rag, rag_chunk_size, rag_chunk_overlap, rag_top_k, rag_fallback)


if __name__ == '__main__':
    main()
