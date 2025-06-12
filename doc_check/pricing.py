"""Pricing information for different LLM providers."""

# OpenAI model pricing (per 1K tokens)
# Source: https://platform.openai.com/docs/pricing
OPENAI_PRICING = {
    # GPT-4.1 series (latest models)
    "gpt-4.1": {"input": 2.00, "output": 8.00},
    "gpt-4.1-2025-04-14": {"input": 2.00, "output": 8.00},
    "gpt-4.1-mini": {"input": 0.40, "output": 1.60},
    "gpt-4.1-mini-2025-04-14": {"input": 0.40, "output": 1.60},
    "gpt-4.1-nano": {"input": 0.10, "output": 0.40},
    "gpt-4.1-nano-2025-04-14": {"input": 0.10, "output": 0.40},
    
    # GPT-4.5 series
    "gpt-4.5-preview": {"input": 75.00, "output": 150.00},
    "gpt-4.5-preview-2025-02-27": {"input": 75.00, "output": 150.00},
    
    # GPT-4o series (excluding reasoning models)
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "gpt-4o-2024-08-06": {"input": 2.50, "output": 10.00},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "gpt-4o-mini-2024-07-18": {"input": 0.15, "output": 0.60},
    
    # Audio and realtime models
    "gpt-4o-audio-preview": {"input": 2.50, "output": 10.00},
    "gpt-4o-audio-preview-2024-12-17": {"input": 2.50, "output": 10.00},
    "gpt-4o-realtime-preview": {"input": 5.00, "output": 20.00},
    "gpt-4o-realtime-preview-2024-12-17": {"input": 5.00, "output": 20.00},
    "gpt-4o-mini-audio-preview": {"input": 0.15, "output": 0.60},
    "gpt-4o-mini-audio-preview-2024-12-17": {"input": 0.15, "output": 0.60},
    "gpt-4o-mini-realtime-preview": {"input": 0.60, "output": 2.40},
    "gpt-4o-mini-realtime-preview-2024-12-17": {"input": 0.60, "output": 2.40},
    
    # Search models
    "gpt-4o-search-preview": {"input": 2.50, "output": 10.00},
    "gpt-4o-search-preview-2025-03-11": {"input": 2.50, "output": 10.00},
    "gpt-4o-mini-search-preview": {"input": 0.15, "output": 0.60},
    "gpt-4o-mini-search-preview-2025-03-11": {"input": 0.15, "output": 0.60},
    
    # Computer use model
    "computer-use-preview": {"input": 3.00, "output": 12.00},
    "computer-use-preview-2025-03-11": {"input": 3.00, "output": 12.00},
    
    # Image generation model
    "gpt-image-1": {"input": 5.00, "output": 0.00},  # No output tokens for image generation
    
    # Codex models
    "codex-mini-latest": {"input": 1.50, "output": 6.00},
    
    # Legacy models
    "gpt-4": {"input": 30.00, "output": 60.00},  # Legacy pricing
    "gpt-4-turbo": {"input": 10.00, "output": 30.00},  # Legacy pricing
    "gpt-3.5-turbo": {"input": 0.50, "output": 1.50},  # Legacy pricing
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
