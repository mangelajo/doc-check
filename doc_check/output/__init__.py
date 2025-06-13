"""Output formatters for doc-check results."""

from .base import OutputFormatter
from .html import HTMLFormatter
from .junit import JUnitFormatter
from .cli import CLIFormatter

__all__ = ['OutputFormatter', 'HTMLFormatter', 'JUnitFormatter', 'CLIFormatter']

# Registry of available formatters
FORMATTERS = {
    'html': HTMLFormatter,
    'junit': JUnitFormatter,
    'cli': CLIFormatter,
}

def get_formatter(format_name: str) -> type[OutputFormatter]:
    """Get formatter class by name."""
    if format_name not in FORMATTERS:
        available = ', '.join(FORMATTERS.keys())
        raise ValueError(f"Unknown output format '{format_name}'. Available formats: {available}")
    return FORMATTERS[format_name]
