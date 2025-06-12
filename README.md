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

2. Set your OpenAI API key:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

3. Run the check:

```bash
doc-check doc-check.yaml
```

## Options

- `--api-key`: OpenAI API key (alternative to environment variable)
- `--model`: OpenAI model to use (default: gpt-4)
- `--verbose, -v`: Show detailed output including full answers
- `--output, -o`: Save results to JSON file

## Example

```bash
doc-check doc-check.yaml --verbose --output results.json
```

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
