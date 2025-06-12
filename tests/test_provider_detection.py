"""Tests for automatic provider detection functionality."""

import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner

from doc_check.core import detect_provider_from_model
from doc_check.cli import check, main


class TestProviderDetection:
    """Test cases for automatic provider detection."""
    
    def test_detect_anthropic_models(self):
        """Test detection of Anthropic models."""
        anthropic_models = [
            "claude-3-5-sonnet-20241022",
            "claude-sonnet-4-20250514", 
            "claude-3-haiku-20240307",
            "claude-3-opus-20240229",
            "CLAUDE-3-SONNET-20240229",  # Test case insensitive
            "some-claude-model",
            "custom-sonnet-variant",
            "haiku-test",
            "opus-custom"
        ]
        
        for model in anthropic_models:
            assert detect_provider_from_model(model) == "anthropic", f"Failed for model: {model}"
    
    def test_detect_openai_models(self):
        """Test detection of OpenAI models."""
        openai_models = [
            "gpt-4",
            "gpt-4-turbo",
            "gpt-3.5-turbo",
            "GPT-4",  # Test case insensitive
            "davinci-002",
            "curie-001",
            "babbage-002",
            "ada-002",
            "custom-gpt-model"
        ]
        
        for model in openai_models:
            assert detect_provider_from_model(model) == "openai", f"Failed for model: {model}"
    
    def test_detect_unknown_models_default_to_openai(self):
        """Test that unknown models default to OpenAI."""
        unknown_models = [
            "unknown-model",
            "custom-llm",
            "some-random-name",
            "",
            "123456"
        ]
        
        for model in unknown_models:
            assert detect_provider_from_model(model) == "openai", f"Failed for model: {model}"
    
    @patch('doc_check.cli.DocumentChecker')
    def test_cli_auto_detection_anthropic(self, mock_checker_class):
        """Test CLI auto-detection for Anthropic models."""
        mock_checker = MagicMock()
        mock_checker_class.return_value = mock_checker
        mock_checker.check_document.return_value = MagicMock(
            failed_questions=0,
            passed_questions=1,
            total_questions=1,
            success_rate=100.0
        )
        
        runner = CliRunner()
        with runner.isolated_filesystem():
            # Create a dummy config file
            with open('config.yaml', 'w') as f:
                f.write("""
file: test.md
questions:
  - name: test
    question: test question
    answerEvaluation: test evaluation
""")
            with open('test.md', 'w') as f:
                f.write("Test document content")
            
            # Test with Claude model but no explicit provider
            result = runner.invoke(check, [
                'config.yaml',
                '--model', 'claude-3-5-sonnet-20241022'
            ])
            
            # Should succeed and auto-detect anthropic
            assert result.exit_code == 0
            
            # Verify DocumentChecker was called with anthropic provider
            mock_checker_class.assert_called_once()
            call_args = mock_checker_class.call_args
            assert call_args[1]['provider'] == 'anthropic'
            assert call_args[1]['model'] == 'claude-3-5-sonnet-20241022'
    
    @patch('doc_check.cli.DocumentChecker')
    def test_cli_auto_detection_openai(self, mock_checker_class):
        """Test CLI auto-detection for OpenAI models."""
        mock_checker = MagicMock()
        mock_checker_class.return_value = mock_checker
        mock_checker.check_document.return_value = MagicMock(
            failed_questions=0,
            passed_questions=1,
            total_questions=1,
            success_rate=100.0
        )
        
        runner = CliRunner()
        with runner.isolated_filesystem():
            # Create a dummy config file
            with open('config.yaml', 'w') as f:
                f.write("""
file: test.md
questions:
  - name: test
    question: test question
    answerEvaluation: test evaluation
""")
            with open('test.md', 'w') as f:
                f.write("Test document content")
            
            # Test with GPT model but no explicit provider
            result = runner.invoke(check, [
                'config.yaml',
                '--model', 'gpt-4-turbo'
            ])
            
            # Should succeed and use openai (default)
            assert result.exit_code == 0
            
            # Verify DocumentChecker was called with openai provider
            mock_checker_class.assert_called_once()
            call_args = mock_checker_class.call_args
            assert call_args[1]['provider'] == 'openai'
            assert call_args[1]['model'] == 'gpt-4-turbo'
    
    @patch('doc_check.cli.DocumentChecker')
    def test_cli_explicit_provider_overrides_detection(self, mock_checker_class):
        """Test that explicit provider setting overrides auto-detection."""
        mock_checker = MagicMock()
        mock_checker_class.return_value = mock_checker
        mock_checker.check_document.return_value = MagicMock(
            failed_questions=0,
            passed_questions=1,
            total_questions=1,
            success_rate=100.0
        )
        
        runner = CliRunner()
        with runner.isolated_filesystem():
            # Create a dummy config file
            with open('config.yaml', 'w') as f:
                f.write("""
file: test.md
questions:
  - name: test
    question: test question
    answerEvaluation: test evaluation
""")
            with open('test.md', 'w') as f:
                f.write("Test document content")
            
            # Test with Claude model but explicit OpenAI provider
            result = runner.invoke(check, [
                'config.yaml',
                '--model', 'claude-3-5-sonnet-20241022',
                '--provider', 'openai'
            ])
            
            # Should succeed and use explicit provider
            assert result.exit_code == 0
            
            # Verify DocumentChecker was called with explicit provider
            mock_checker_class.assert_called_once()
            call_args = mock_checker_class.call_args
            assert call_args[1]['provider'] == 'openai'  # Explicit override
            assert call_args[1]['model'] == 'claude-3-5-sonnet-20241022'
    
    @patch('doc_check.cli.DocumentChecker')
    def test_main_function_auto_detection(self, mock_checker_class):
        """Test auto-detection in the main function."""
        mock_checker = MagicMock()
        mock_checker_class.return_value = mock_checker
        mock_checker.check_document.return_value = MagicMock(
            failed_questions=0,
            passed_questions=1,
            total_questions=1,
            success_rate=100.0
        )
        
        runner = CliRunner()
        with runner.isolated_filesystem():
            # Create a dummy config file
            with open('config.yaml', 'w') as f:
                f.write("""
file: test.md
questions:
  - name: test
    question: test question
    answerEvaluation: test evaluation
""")
            with open('test.md', 'w') as f:
                f.write("Test document content")
            
            # Test main function with Claude model
            result = runner.invoke(main, [
                'config.yaml',
                '--model', 'claude-3-haiku-20240307'
            ])
            
            # Should succeed and auto-detect anthropic
            assert result.exit_code == 0
            
            # Verify DocumentChecker was called with anthropic provider
            mock_checker_class.assert_called_once()
            call_args = mock_checker_class.call_args
            assert call_args[1]['provider'] == 'anthropic'
            assert call_args[1]['model'] == 'claude-3-haiku-20240307'
    
    def test_edge_cases(self):
        """Test edge cases for provider detection."""
        # Test models with multiple keywords
        assert detect_provider_from_model("claude-gpt-hybrid") == "anthropic"  # Claude takes precedence
        assert detect_provider_from_model("gpt-sonnet-mix") == "anthropic"  # Sonnet takes precedence
        
        # Test partial matches
        assert detect_provider_from_model("my-claude-model") == "anthropic"
        assert detect_provider_from_model("custom-gpt") == "openai"
        
        # Test whitespace and special characters
        assert detect_provider_from_model("  claude-3-sonnet  ") == "anthropic"
        assert detect_provider_from_model("gpt_4_turbo") == "openai"
        assert detect_provider_from_model("claude-3.5-sonnet") == "anthropic"
