from typing import Optional

from app.config import settings
from app.llm.base import BaseLLMProvider
from app.llm.providers import AnthropicProvider, GeminiProvider, OpenAIProvider
from app.llm.types import LLMModel, LLMProvider


class LLMProviderFactory:
    DEFAULT_MODELS: dict[LLMProvider, LLMModel] = {
        LLMProvider.OPENAI: LLMModel.GPT_4O,
        LLMProvider.ANTHROPIC: LLMModel.CLAUDE_SONNET_4,
        LLMProvider.GEMINI: LLMModel.GEMINI_2_FLASH,
    }

    PROVIDERS: dict[LLMProvider, type[BaseLLMProvider]] = {
        LLMProvider.OPENAI: OpenAIProvider,
        LLMProvider.ANTHROPIC: AnthropicProvider,
        LLMProvider.GEMINI: GeminiProvider,
    }

    @classmethod
    def create_provider(
        cls,
        provider: str,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
    ) -> BaseLLMProvider:
        provider_enum = LLMProvider(provider)
        provider_class = cls.PROVIDERS[provider_enum]

        resolved_model = model or cls.DEFAULT_MODELS[provider_enum].value
        resolved_temperature = temperature or settings.DEFAULT_TEMPERATURE

        return provider_class(model=resolved_model, temperature=resolved_temperature)

    @classmethod
    def get_default_provider(cls) -> BaseLLMProvider:
        return cls.create_provider(
            provider=settings.DEFAULT_LLM_PROVIDER,
            model=settings.DEFAULT_LLM_MODEL,
            temperature=settings.DEFAULT_TEMPERATURE,
        )
