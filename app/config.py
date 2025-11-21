import os
from typing import Optional

from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv())

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    DEFAULT_LLM_PROVIDER: str = os.getenv("DEFAULT_LLM_PROVIDER")
    DEFAULT_LLM_MODEL: Optional[str] = os.getenv("DEFAULT_LLM_MODEL")
    DEFAULT_TEMPERATURE: float = os.getenv("DEFAULT_TEMPERATURE")

    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    GOOGLE_API_KEY: Optional[str] = os.getenv("GOOGLE_API_KEY")

    LANGCHAIN_TRACING_V2: bool = os.getenv("LANGCHAIN_TRACING_V2")
    LANGCHAIN_API_KEY: Optional[str] = os.getenv("LANGCHAIN_API_KEY")
    LANGCHAIN_PROJECT: str = os.getenv("LANGCHAIN_PROJECT")

    API_HOST: str = os.getenv("API_HOST")
    API_PORT: int = os.getenv("API_PORT")


settings = Settings()
