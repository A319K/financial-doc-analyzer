from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # App
    APP_NAME: str = "Financial Document Analyzer"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/financial_analyzer"

    # JWT
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # LLM
    OPENAI_API_KEY: str = ""

    # Vector DB
    PINECONE_API_KEY: str = ""
    PINECONE_ENVIRONMENT: str = "us-east1-aws"

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()