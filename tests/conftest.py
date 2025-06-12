"""Pytest configuration and fixtures for doc-check tests."""

import pytest
import tempfile
import os
from pathlib import Path


@pytest.fixture
def temp_config_file():
    """Create a temporary config file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write("""
file: test_document.md
questions:
  - name: "Test Question"
    question: "What is this document about?"
    answerEvaluation: "Answer should mention the main topic"
""")
        temp_path = Path(f.name)
    
    yield temp_path
    
    # Cleanup
    if temp_path.exists():
        temp_path.unlink()


@pytest.fixture
def temp_document_file():
    """Create a temporary document file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write("# Test Document\n\nThis is a test document for unit testing.")
        temp_path = Path(f.name)
    
    yield temp_path
    
    # Cleanup
    if temp_path.exists():
        temp_path.unlink()
