"""Anthropic provider for document checking."""

import os
import re
from typing import Optional

import anthropic

from ..models import ApiUsage
from ..pricing import ANTHROPIC_PRICING

# System prompts
QUESTION_ANSWERING_SYSTEM_PROMPT = """You are a helpful assistant that answers questions about documentation accurately
and comprehensively. Don't propose alternative solutions which aren't explicitly documented.
"""
EVALUATION_SYSTEM_PROMPT = "You are an expert evaluator. Carefully assess whether the answer meets the specified criteria. Be strict but fair in your evaluation."
SUMMARIZATION_SYSTEM_PROMPT = "You are an expert document cleaner. Update the document according to the instructions provided by the user."

# Question answering prompt template
QUESTION_PROMPT_TEMPLATE = """Based on the following document, please answer this question:

Question: {question}

Document:
{document_content}

Please provide a comprehensive answer based on the information in the document, do not provide alternatives outside of the explicit
examples in the documentation."""

# Evaluation prompt template
EVALUATION_PROMPT_TEMPLATE = """Please evaluate the following answer against the given criteria.

Question: {question}

Answer: {answer}

Evaluation Criteria: {evaluation_criteria}

Please respond with:
1. PASS or FAIL
2. A brief explanation of your evaluation

Format your response as:
RESULT: [PASS/FAIL]
EXPLANATION: [Your explanation]"""

# API configuration
ANTHROPIC_MAX_TOKENS = 4000
ANTHROPIC_SUMMARIZER_MAX_TOKENS = 8000
DEFAULT_TEMPERATURE = 0.1
DEFAULT_ANTHROPIC_MODEL = "claude-sonnet-4-20250514"


class AnthropicProvider:
    """Provider for Anthropic API interactions."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = DEFAULT_ANTHROPIC_MODEL):
        """Initialize the Anthropic provider.
        
        Args:
            api_key: Anthropic API key. If None, will try to get from environment.
            model: Model to use for evaluation.
        """
        self.client = anthropic.Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))
        self.model = model
        self.api_usage = ApiUsage(provider="anthropic", model=model)
    
    def ask(self, document_content: str, question: str) -> str:
        """Ask a question about the document using Anthropic API."""
        prompt = QUESTION_PROMPT_TEMPLATE.format(
            question=question,
            document_content=document_content
        )

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=ANTHROPIC_MAX_TOKENS,
                temperature=DEFAULT_TEMPERATURE,
                system=QUESTION_ANSWERING_SYSTEM_PROMPT,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            # Track usage
            if response.usage:
                self.api_usage.input_tokens += response.usage.input_tokens
                self.api_usage.output_tokens += response.usage.output_tokens
                self.api_usage.total_tokens += response.usage.input_tokens + response.usage.output_tokens
                self.api_usage.api_calls += 1
                self.api_usage.estimated_cost += self._calculate_cost(response.usage)
            
            # Store raw response for debug mode
            self.last_raw_response = response.content[0].text
            
            return response.content[0].text
        except Exception as e:
            raise RuntimeError(f"Failed to get answer from Anthropic: {e}")
    
    def evaluate(self, question: str, answer: str, evaluation_criteria: str) -> tuple[bool, str]:
        """Evaluate an answer against criteria using Anthropic API."""
        prompt = EVALUATION_PROMPT_TEMPLATE.format(
            question=question,
            answer=answer,
            evaluation_criteria=evaluation_criteria
        )

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                temperature=DEFAULT_TEMPERATURE,
                system=EVALUATION_SYSTEM_PROMPT,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            # Track usage
            if response.usage:
                self.api_usage.input_tokens += response.usage.input_tokens
                self.api_usage.output_tokens += response.usage.output_tokens
                self.api_usage.total_tokens += response.usage.input_tokens + response.usage.output_tokens
                self.api_usage.api_calls += 1
                self.api_usage.estimated_cost += self._calculate_cost(response.usage)
            
            evaluation_text = response.content[0].text
            
            # Store raw response for debug mode
            self.last_raw_response = evaluation_text
            
            return self._parse_evaluation_result(evaluation_text)
            
        except Exception as e:
            raise RuntimeError(f"Failed to evaluate answer with Anthropic: {e}")
    
    def summarize(self, document_content: str) -> str:
        """Summarize document content using Anthropic API."""
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=ANTHROPIC_SUMMARIZER_MAX_TOKENS,
                temperature=DEFAULT_TEMPERATURE,
                system=SUMMARIZATION_SYSTEM_PROMPT,
                messages=[
                    {"role": "user", "content": document_content}
                ]
            )
            
            # Track usage
            if response.usage:
                self.api_usage.input_tokens += response.usage.input_tokens
                self.api_usage.output_tokens += response.usage.output_tokens
                self.api_usage.total_tokens += response.usage.input_tokens + response.usage.output_tokens
                self.api_usage.api_calls += 1
                self.api_usage.estimated_cost += self._calculate_cost(response.usage)
            
            return response.content[0].text
        except Exception as e:
            raise RuntimeError(f"Failed to summarize document with Anthropic: {e}")
    
    def _calculate_cost(self, usage) -> float:
        """Calculate estimated cost for Anthropic API usage."""
        # Default to sonnet 4 pricing if model not found
        model_pricing = ANTHROPIC_PRICING.get(self.model, ANTHROPIC_PRICING[DEFAULT_ANTHROPIC_MODEL])
        
        input_cost = (usage.input_tokens / 1000) * model_pricing["input"]
        output_cost = (usage.output_tokens / 1000) * model_pricing["output"]
        
        return input_cost + output_cost
    
    def _parse_evaluation_result(self, evaluation_text: str) -> tuple[bool, str]:
        """Parse the evaluation result from LLM response."""
        # Improved parsing with multiple strategies
        passed = False
        explanation = evaluation_text
        
        # Strategy 1: Look for structured format
        result_match = re.search(r'RESULT:\s*(PASS|FAIL)', evaluation_text, re.IGNORECASE)
        explanation_match = re.search(r'EXPLANATION:\s*(.+?)(?:\n\n|\Z)', evaluation_text, re.IGNORECASE | re.DOTALL)
        
        if result_match:
            passed = result_match.group(1).upper() == 'PASS'
            if explanation_match:
                explanation = explanation_match.group(1).strip()
        else:
            # Strategy 2: Look for pass/fail patterns in text
            pass_indicators = ['PASS', 'passes', 'meets the criteria', 'satisfies', 'adequate', 'sufficient']
            fail_indicators = ['FAIL', 'fails', 'does not meet', 'insufficient', 'inadequate', 'missing']
            
            text_upper = evaluation_text.upper()
            pass_count = sum(1 for indicator in pass_indicators if indicator.upper() in text_upper)
            fail_count = sum(1 for indicator in fail_indicators if indicator.upper() in text_upper)
            
            # If we have clear indicators, use them
            if pass_count > fail_count:
                passed = True
            elif fail_count > pass_count:
                passed = False
            else:
                # Strategy 3: Look at the overall sentiment/tone
                positive_words = ['good', 'correct', 'accurate', 'comprehensive', 'detailed', 'complete']
                negative_words = ['poor', 'incorrect', 'inaccurate', 'incomplete', 'missing', 'lacks']
                
                positive_count = sum(1 for word in positive_words if word in text_upper)
                negative_count = sum(1 for word in negative_words if word in text_upper)
                
                passed = positive_count > negative_count
        
        return passed, explanation
