from abc import ABC, abstractmethod
from typing import Optional

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import BaseMessage


class BaseLLMProvider(ABC):
    def __init__(self, model: Optional[str] = None, temperature: float = 0.7) -> None:
        self.model = model or self.get_default_model()
        self.temperature = temperature

    @abstractmethod
    def get_default_model(self) -> str:
        pass

    @abstractmethod
    def get_chat_model(self) -> Optional[BaseChatModel]:
        pass

    def generate(self, system_prompt: str, user_prompt: str, **kwargs: str) -> str:
        llm = self.get_chat_model()
        if llm is None:
            return ""

        from langchain_core.messages import HumanMessage, SystemMessage

        messages: list[BaseMessage] = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt),
        ]

        response = llm.invoke(messages)
        return str(response.content)

    def generate_with_messages(self, messages: list[BaseMessage]) -> str:
        llm = self.get_chat_model()
        if llm is None:
            return ""

        response = llm.invoke(messages)
        return str(response.content)
