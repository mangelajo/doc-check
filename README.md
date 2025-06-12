# Doc-Check

A CLI tool for checking documentation quality using LLM-based Q&A evaluation.

## Installation

### Using uv (recommended)

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install the package in development mode
uv pip install -e .
```

### Using pip

```bash
pip install -e .
```

## Usage

### Commands

Doc-Check provides several commands:

- `doc-check check`: Check documentation quality using LLM evaluation
- `doc-check validate`: Validate configuration file format
- `doc-check main`: Alternative entry point for checking (same as check)

### Basic Usage

1. Create a `doc-check.yaml` configuration file:

```yaml
file: output.md
questions:
   - name: installation options
     question: |
       What are the install options for jumpstarter?
     answerEvaluation: |
       The answer should contain details on installing jumpstarter with pip locally,
       but also explain that the distributed service can be installed with helm or
       argoCD into a cluster.
```

2. Set your API key (OpenAI or Anthropic):

```bash
export OPENAI_API_KEY="your-api-key-here"
# OR
export ANTHROPIC_API_KEY="your-api-key-here"
```

3. Run the check:

```bash
doc-check check doc-check.yaml
```

### Check Command Options

- `--api-key`: API key (alternative to environment variable)
- `--model`: Model to use (auto-detects provider from model name)
- `--provider`: Explicitly specify provider (openai or anthropic)
- `--verbose, -v`: Show detailed output including full answers
- `--output, -o`: Save results to file
- `--format`: Output format (json, yaml, or auto)
- `--summarize`: Summarization level (minimal, moderate, aggressive)
- `--summarizer-model`: Model to use for document summarization

### Validate Command

Validate your configuration file:

```bash
doc-check validate doc-check.yaml
```

## Examples

```bash
# Basic check with verbose output
doc-check check doc-check.yaml --verbose

# Save results to JSON file
doc-check check doc-check.yaml --output results.json

# Use specific model and provider
doc-check check doc-check.yaml --model gpt-4.1 --provider openai

# Use Anthropic Claude
doc-check check doc-check.yaml --model claude-sonnet-4-20250514

# Summarize document before checking (for large documents)
doc-check check doc-check.yaml --summarize minimal

# Validate configuration only
doc-check validate doc-check.yaml
```

## Supported Models and Providers

Doc-Check supports both OpenAI and Anthropic models with automatic provider detection:

### OpenAI Models
- `gpt-4.1` (default)
- `gpt-4.1-mini`
- `gpt-4.1-nano`
- `gpt-4.5-turbo`
- And other GPT models

### Anthropic Models
- `claude-sonnet-4-20250514` (default for Anthropic)
- `claude-opus-4`
- `claude-sonnet-3.7`
- `claude-3-5-sonnet-20241022`
- And other Claude models

The provider is automatically detected from the model name, or you can specify it explicitly with `--provider`.

## Configuration Format

The configuration file should contain:

- `file`: Path to the document to check (relative to config file)
- `questions`: List of questions with:
  - `name`: Unique identifier for the question
  - `question`: The question to ask about the document
  - `answerEvaluation`: Criteria for evaluating the answer

## Exit Codes

- `0`: All questions passed
- `1`: One or more questions failed or an error occurred

## Development

### Using uv for development

```bash
# Install development dependencies
uv pip install -e ".[dev]"

# Run tests
uv run pytest

# Format code
uv run black .
uv run isort .

# Type checking
uv run mypy doc_check
```
