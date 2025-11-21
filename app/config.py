from typing import Optional

from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv())

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    DEFAULT_LLM_PROVIDER: Optional[str] = None
    DEFAULT_LLM_MODEL: Optional[int] = None
    DEFAULT_TEMPERATURE: Optional[str] = None

    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    GOOGLE_API_KEY: Optional[str] = None

    LANGCHAIN_TRACING_V2: bool = False
    LANGCHAIN_API_KEY: Optional[str] = None
    LANGCHAIN_PROJECT: str = 'default-project'

    API_HOST: str = "localhost"
    API_PORT: int = 8000


settings = Settings()
