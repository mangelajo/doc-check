"""Output formatters for doc-check results."""

from .base import OutputFormatter
from .html import HTMLFormatter
from .junit import JUnitFormatter

__all__ = ['OutputFormatter', 'HTMLFormatter', 'JUnitFormatter']

# Registry of available formatters
FORMATTERS = {
    'html': HTMLFormatter,
    'junit': JUnitFormatter,
}

def get_formatter(format_name: str) -> type[OutputFormatter]:
    """Get formatter class by name."""
    if format_name not in FORMATTERS:
        available = ', '.join(FORMATTERS.keys())
        raise ValueError(f"Unknown output format '{format_name}'. Available formats: {available}")
    return FORMATTERS[format_name]
