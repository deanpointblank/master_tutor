from typing import Optional

from langchain_core.language_models import BaseChatModel
from pydantic import SecretStr
from tenacity import retry, stop_after_attempt, wait_exponential

from app.config import settings
from app.llm.base import BaseLLMProvider
from app.llm.types import LLMModel


class OpenAIProvider(BaseLLMProvider):
    def get_default_model(self) -> str:
        return LLMModel.GPT_4O.value

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def get_chat_model(self) -> Optional[BaseChatModel]:
        if not settings.OPENAI_API_KEY:
            return None

        from langchain_openai import ChatOpenAI

        return ChatOpenAI(
            model=self.model,
            temperature=self.temperature,
            api_key=SecretStr(settings.OPENAI_API_KEY),
        )
