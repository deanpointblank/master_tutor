from typing import Optional

from langchain_core.language_models import BaseChatModel
from tenacity import retry, stop_after_attempt, wait_exponential

from app.config import settings
from app.llm.base import BaseLLMProvider
from app.llm.types import LLMModel


class GeminiProvider(BaseLLMProvider):
    def get_default_model(self) -> str:
        return LLMModel.GEMINI_2_FLASH.value

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def get_chat_model(self) -> Optional[BaseChatModel]:
        if not settings.GOOGLE_API_KEY:
            return None

        from langchain_google_genai import ChatGoogleGenerativeAI

        return ChatGoogleGenerativeAI(
            model=self.model,
            temperature=self.temperature,
            google_api_key=settings.GOOGLE_API_KEY,
        )
