"""Base interface for output formatters."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional

from ..models import DocCheckResult


class OutputFormatter(ABC):
    """Base class for output formatters."""
    
    def __init__(self, output_dir: Optional[Path] = None):
        """Initialize the formatter.
        
        Args:
            output_dir: Directory to write output files to. If None, uses current directory.
        """
        self.output_dir = output_dir or Path.cwd()
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    @abstractmethod
    def write_results(self, result: DocCheckResult, filename: Optional[str] = None) -> Path:
        """Write the results to a file.
        
        Args:
            result: The test results to write
            filename: Optional filename override. If None, uses default naming.
            
        Returns:
            Path to the written file
        """
        pass
    
    @property
    @abstractmethod
    def default_filename(self) -> str:
        """Default filename for this formatter."""
        pass
    
    @property
    @abstractmethod
    def file_extension(self) -> str:
        """File extension for this formatter."""
        pass
