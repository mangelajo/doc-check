"""Data models for doc-check."""

from typing import List, Optional
from pydantic import BaseModel


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


class DocCheckResult(BaseModel):
    """Overall result of document checking."""
    total_questions: int
    passed_questions: int
    failed_questions: int
    results: List[QuestionResult]
    
    @property
    def success_rate(self) -> float:
        """Calculate success rate as percentage."""
        if self.total_questions == 0:
            return 0.0
        return (self.passed_questions / self.total_questions) * 100
