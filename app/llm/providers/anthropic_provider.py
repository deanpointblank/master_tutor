from typing import Optional

from langchain_core.language_models import BaseChatModel
from pydantic import SecretStr
from tenacity import retry, stop_after_attempt, wait_exponential

from app.config import settings
from app.llm.base import BaseLLMProvider
from app.llm.types import LLMModel


class AnthropicProvider(BaseLLMProvider):
    def get_default_model(self) -> str:
        return LLMModel.CLAUDE_SONNET_4.value

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def get_chat_model(self) -> Optional[BaseChatModel]:
        if not settings.ANTHROPIC_API_KEY:
            return None

        from langchain_anthropic import ChatAnthropic

        return ChatAnthropic(
            model_name=self.model,
            temperature=self.temperature,
            api_key=SecretStr(settings.ANTHROPIC_API_KEY),
            timeout=None,
            stop=None,
        )
