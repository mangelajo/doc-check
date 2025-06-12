"""Pricing information for different LLM providers."""

# OpenAI model pricing (per 1K tokens)
# Source: https://platform.openai.com/docs/pricing
OPENAI_PRICING = {
    # GPT-4.1 series (latest models)
    "gpt-4.1": {"input": 0.002, "output": 0.008},
    "gpt-4.1-2025-04-14": {"input": 0.002, "output": 0.008},
    "gpt-4.1-mini": {"input": 0.0004, "output": 0.0016},
    "gpt-4.1-mini-2025-04-14": {"input": 0.0004, "output": 0.0016},
    "gpt-4.1-nano": {"input": 0.0001, "output": 0.0004},
    "gpt-4.1-nano-2025-04-14": {"input": 0.0001, "output": 0.0004},
    
    # GPT-4.5 series
    "gpt-4.5-preview": {"input": 0.075, "output": 0.15},
    "gpt-4.5-preview-2025-02-27": {"input": 0.075, "output": 0.15},
    
    # GPT-4o series (excluding reasoning models)
    "gpt-4o": {"input": 0.0025, "output": 0.01},
    "gpt-4o-2024-08-06": {"input": 0.0025, "output": 0.01},
    "gpt-4o-mini": {"input": 0.00015, "output": 0.0006},
    "gpt-4o-mini-2024-07-18": {"input": 0.00015, "output": 0.0006},
    
    # Audio and realtime models
    "gpt-4o-audio-preview": {"input": 0.0025, "output": 0.01},
    "gpt-4o-audio-preview-2024-12-17": {"input": 0.0025, "output": 0.01},
    "gpt-4o-realtime-preview": {"input": 0.005, "output": 0.02},
    "gpt-4o-realtime-preview-2024-12-17": {"input": 0.005, "output": 0.02},
    "gpt-4o-mini-audio-preview": {"input": 0.00015, "output": 0.0006},
    "gpt-4o-mini-audio-preview-2024-12-17": {"input": 0.00015, "output": 0.0006},
    "gpt-4o-mini-realtime-preview": {"input": 0.0006, "output": 0.0024},
    "gpt-4o-mini-realtime-preview-2024-12-17": {"input": 0.0006, "output": 0.0024},
    
    # Search models
    "gpt-4o-search-preview": {"input": 0.0025, "output": 0.01},
    "gpt-4o-search-preview-2025-03-11": {"input": 0.0025, "output": 0.01},
    "gpt-4o-mini-search-preview": {"input": 0.00015, "output": 0.0006},
    "gpt-4o-mini-search-preview-2025-03-11": {"input": 0.00015, "output": 0.0006},
    
    # Computer use model
    "computer-use-preview": {"input": 0.003, "output": 0.012},
    "computer-use-preview-2025-03-11": {"input": 0.003, "output": 0.012},
    
    # Image generation model
    "gpt-image-1": {"input": 0.005, "output": 0.00},  # No output tokens for image generation
    
    # Codex models
    "codex-mini-latest": {"input": 0.0015, "output": 0.006},
    
    # Legacy models
    "gpt-4": {"input": 0.03, "output": 0.06},  # Legacy pricing
    "gpt-4-turbo": {"input": 0.01, "output": 0.03},  # Legacy pricing
    "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},  # Legacy pricing
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
