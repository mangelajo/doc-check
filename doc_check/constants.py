"""Constants for doc-check to avoid repetition."""

# System prompts
QUESTION_ANSWERING_SYSTEM_PROMPT = "You are a helpful assistant that answers questions about documentation accurately and comprehensively."

EVALUATION_SYSTEM_PROMPT = "You are an expert evaluator. Carefully assess whether the answer meets the specified criteria. Be strict but fair in your evaluation."

SUMMARIZATION_SYSTEM_PROMPT = "You are an expert document summarizer. Create comprehensive, detailed summaries that preserve all important information."

# Question answering prompt template
QUESTION_PROMPT_TEMPLATE = """Based on the following document, please answer this question:

Question: {question}

Document:
{document_content}

Please provide a comprehensive answer based on the information in the document."""

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

# Summarization prompt templates
SUMMARIZATION_PROMPTS = {
    "minimal": """Please provide a minimal summary of the following document. The summary should:
1. Preserve nearly all key information, concepts, and details
2. Maintain the exact structure and organization of the original
3. Include all technical details, examples, and specifications
4. Be comprehensive enough to answer any detailed questions about the document's content
5. Preserve all code examples, configuration details, and specific instructions
6. Only remove redundant phrases and minor formatting - aim to reduce length by about 5-10% while keeping all essential content

Document to summarize:
{document_content}

Please provide a very detailed summary that retains virtually all essential information needed to answer questions about this document.""",

    "light": """Please provide a light summary of the following document. The summary should:
1. Preserve most key information, concepts, and details
2. Maintain the structure and organization of the original
3. Include all important technical details, examples, and specifications
4. Be comprehensive enough to answer detailed questions about the document's content
5. Preserve all code examples, configuration details, and specific instructions
6. Aim to reduce length by about 20-30% while keeping essential details

Document to summarize:
{document_content}

Please provide a detailed summary that retains nearly all essential information needed to answer questions about this document.""",

    "medium": """Please provide a balanced summary of the following document. The summary should:
1. Capture the most important information, concepts, and key details
2. Maintain the overall structure but condense sections appropriately
3. Include critical technical details and key examples
4. Be detailed enough to answer most questions about the document's content
5. Preserve essential code examples and important configuration details
6. Aim to reduce length by about 50% while keeping important information

Document to summarize:
{document_content}

Please provide a well-balanced summary that retains the important information needed to answer questions about this document.""",

    "aggressive": """Please provide a high-level summary of the following document. The summary should:
1. Focus on the main concepts, key points, and essential information only
2. Provide a condensed overview of the document's structure and purpose
3. Include only the most critical technical details and examples
4. Cover the core topics at a level sufficient for general understanding
5. Preserve only the most essential code examples or configuration details
6. Aim to reduce length by about 70-80% while keeping core concepts

Document to summarize:
{document_content}

Please provide a concise, high-level summary that captures the essential concepts and main points of this document."""
}

# Default models
DEFAULT_OPENAI_MODEL = "gpt-4"
DEFAULT_ANTHROPIC_MODEL = "claude-sonnet-4-20250514"
DEFAULT_SUMMARIZER_MODEL = "claude-sonnet-4-20250514"

# API configuration
OPENAI_MAX_TOKENS = 4000
ANTHROPIC_MAX_TOKENS = 4000
ANTHROPIC_SUMMARIZER_MAX_TOKENS = 8000
DEFAULT_TEMPERATURE = 0.1

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
