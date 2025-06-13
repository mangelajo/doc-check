"""Ollama provider for local LLM interactions."""

import json
import requests
from typing import Optional, Tuple
from ..models import ApiUsage
from ..pricing import OLLAMA_PRICING

QUESTION_ANSWERING_SYSTEM_PROMPT = """You are a helpful assistant that answers questions about documents accurately and comprehensively. Don't propose alternative solutions which aren't explicitly documented."""

EVALUATION_SYSTEM_PROMPT = """You are an expert evaluator.
Carefully assess whether the answer meets the specified criteria.
Be strict but fair in your evaluation."""

SUMMARIZATION_SYSTEM_PROMPT = "You are an expert document summarizer. Create comprehensive, detailed summaries that preserve all important information."

QUESTION_PROMPT_TEMPLATE = """Based on the following document, please answer this question:

Question: {question}

Document:
{document_content}

Please provide a comprehensive answer based on the information in the document, do not provide alternative solutions which aren't explicitly documented."""

EVALUATION_PROMPT_TEMPLATE = """Please evaluate the following answer against the given criteria.

Question: {question}

Answer: {answer}

Evaluation Criteria: {evaluation_criteria}

Please respond with:
1. PASS (if meets the criteria) or FAIL (Doesn't meet the criteria)
2. Brief explanation of your evaluation

Format your response as:
RESULT: [PASS/FAIL]
EXPLANATION: [Your explanation]"""

DEFAULT_TEMPERATURE = 0.1
DEFAULT_OLLAMA_MODEL = "llama3.2"
DEFAULT_OLLAMA_BASE_URL = "http://localhost:11434"


class OllamaProvider:
    """Provider for Ollama local LLM interactions."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = DEFAULT_OLLAMA_MODEL, base_url: str = DEFAULT_OLLAMA_BASE_URL):
        self.model = model
        self.base_url = base_url.rstrip('/')
        self.api_usage = ApiUsage(provider="ollama", model=model)
    
    def ask(self, document_content: str, question: str) -> str:
        """Ask a question about the document content."""
        prompt = QUESTION_PROMPT_TEMPLATE.format(
            question=question,
            document_content=document_content
        )
        
        response = self._make_request(prompt, QUESTION_ANSWERING_SYSTEM_PROMPT)
        return response
    
    def evaluate(self, question: str, answer: str, evaluation_criteria: str) -> Tuple[bool, str]:
        """Evaluate an answer against the given criteria."""
        prompt = EVALUATION_PROMPT_TEMPLATE.format(
            question=question,
            answer=answer,
            evaluation_criteria=evaluation_criteria
        )
        
        evaluation_text = self._make_request(prompt, EVALUATION_SYSTEM_PROMPT)
        return self._parse_evaluation_result(evaluation_text)
    
    def summarize(self, document_content: str) -> str:
        """Summarize the document content."""
        prompt = f"Please summarize the following document:\n\n{document_content}"
        return self._make_request(prompt, SUMMARIZATION_SYSTEM_PROMPT)
    
    def _make_request(self, prompt: str, system_prompt: str) -> str:
        """Make a request to the Ollama API."""
        url = f"{self.base_url}/api/generate"
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system_prompt,
            "stream": False,
            "options": {
                "temperature": DEFAULT_TEMPERATURE
            }
        }
        
        try:
            response = requests.post(url, json=payload, timeout=300)
            response.raise_for_status()
            
            result = response.json()
            
            # Track token usage if available
            input_tokens = result.get('prompt_eval_count', 0)
            output_tokens = result.get('eval_count', 0)
            
            self.api_usage.input_tokens += input_tokens
            self.api_usage.output_tokens += output_tokens
            self.api_usage.total_tokens += input_tokens + output_tokens
            self.api_usage.api_calls += 1
            self.api_usage.estimated_cost += self._calculate_cost(result)
            
            return result.get('response', '')
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ollama API request failed: {str(e)}")
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to parse Ollama API response: {str(e)}")
    
    def _calculate_cost(self, response_data) -> float:
        """Calculate the cost of the API call (Ollama is free)."""
        # Ollama is free to use locally, so cost is always 0
        return 0.0
    
    def _parse_evaluation_result(self, evaluation_text: str) -> Tuple[bool, str]:
        """Parse the evaluation result from the LLM response."""
        lines = evaluation_text.strip().split('\n')
        
        result = False
        explanation = evaluation_text
        
        for line in lines:
            line = line.strip()
            if line.startswith('RESULT:'):
                result_text = line.replace('RESULT:', '').strip().upper()
                result = result_text == 'PASS'
            elif line.startswith('EXPLANATION:'):
                explanation = line.replace('EXPLANATION:', '').strip()
        
        return result, explanation
