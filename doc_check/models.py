"""Data models for doc-check."""

from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class Question(BaseModel):
    """A single question with its evaluation criteria."""
    name: str
    question: str
    answerEvaluation: str


class DocCheckConfig(BaseModel):
    """Configuration for document checking."""
    file: str
    questions: List[Question]


class QuestionResult(BaseModel):
    """Result of a single question evaluation."""
    name: str
    question: str
    answer: str
    evaluation_result: str
    passed: bool
    error: Optional[str] = None


class ApiUsage(BaseModel):
    """Track API usage and costs."""
    
    provider: str  # "openai" or "anthropic"
    model: str
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    estimated_cost: float = 0.0  # in USD
    api_calls: int = 0


class DocCheckResult(BaseModel):
    """Overall result of document checking."""
    total_questions: int
    passed_questions: int
    failed_questions: int
    results: List[QuestionResult]
    api_usage: Optional[ApiUsage] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    summarization_level: Optional[str] = None
    
    @property
    def success_rate(self) -> float:
        """Calculate success rate as percentage."""
        if self.total_questions == 0:
            return 0.0
        return (self.passed_questions / self.total_questions) * 100
    
    @property
    def duration_seconds(self) -> Optional[float]:
        """Calculate duration in seconds."""
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return None
