import os
from pydantic_settings import BaseSettings,SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    APP_NAME : str = os.getenv("APP_NAME")
    APP_VERSION : str = os.getenv('APP_VERSION')
    DEBUG : bool = os.getenv("DEBUG")

    DB_HOST : str = os.getenv("DB_HOST")
    DB_USER : str = os.getenv("DB_USER")
    DB_PORT : int = os.getenv("DB_PORT")
    DB_NAME : str = os.getenv("DB_NAME")
    DB_PASSWORD : str = os.getenv("DB_PASSWORD")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"

    )

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()