from enum import Enum


class LLMProvider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GEMINI = "gemini"


class LLMModel(str, Enum):
    GPT_4O = "gpt-4o"
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_O1 = "o1"
    GPT_O1_MINI = "o1-mini"

    CLAUDE_SONNET_4 = "claude-sonnet-4-20250514"
    CLAUDE_OPUS_4 = "claude-opus-4-20250514"
    CLAUDE_HAIKU_4 = "claude-haiku-4-20250316"

    GEMINI_2_FLASH = "gemini-2.0-flash-exp"
    GEMINI_15_PRO = "gemini-1.5-pro"
    GEMINI_15_FLASH = "gemini-1.5-flash"
