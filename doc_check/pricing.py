"""Pricing information for different LLM providers."""

# Model pricing (per 1K tokens)
OPENAI_PRICING = {
    "gpt-4": {"input": 0.03, "output": 0.06},
    "gpt-4-turbo": {"input": 0.01, "output": 0.03},
    "gpt-3.5-turbo": {"input": 0.0015, "output": 0.002},
}

# Anthropic pricing as of December 2024 (per 1K tokens)
# Source: https://docs.anthropic.com/en/docs/about-claude/pricing
ANTHROPIC_PRICING = {
    # Claude 4 models
    "claude-opus-4": {"input": 0.015, "output": 0.075},
    "claude-sonnet-4": {"input": 0.003, "output": 0.015},
    "claude-sonnet-4-20250514": {"input": 0.003, "output": 0.015},
    
    # Claude 3.7 models
    "claude-sonnet-3.7": {"input": 0.003, "output": 0.015},
    
    # Claude 3.5 models
    "claude-3-5-sonnet-20241022": {"input": 0.003, "output": 0.015},
    "claude-3-5-sonnet-20240620": {"input": 0.003, "output": 0.015},
    "claude-haiku-3.5": {"input": 0.0008, "output": 0.004},
    
    # Claude 3 models
    "claude-3-opus-20240229": {"input": 0.015, "output": 0.075},
    "claude-3-sonnet-20240229": {"input": 0.003, "output": 0.015},
    "claude-3-haiku-20240307": {"input": 0.00025, "output": 0.00125},
}
