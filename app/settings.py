import os
from typing import ClassVar, Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from .logger import get_logger

logger = get_logger()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="",
        case_sensitive=True,
        populate_by_name=True,
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    ENVIRONMENT: str = "development"
    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
    APP_NAME: str = "Multi tenancy API"

    # Required DB env vars
    DB_USER: str = Field(..., description="Database username")
    DB_NAME: str = Field(..., description="Database name")
    DB_PASS: str = Field(..., description="Database password")
    DB_HOST: str = Field(..., description="Database host")
    DB_PORT: str = Field(..., description="Database port")

    _instance: ClassVar[Optional["Settings"]] = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            logger.info("Creating new Settings instance")
            print(f"\n{__name__}=====> \033[92mSettings __new__\033[0m\n")
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def instance(cls) -> "Settings":
        logger.info("Accessing Settings instance")
        print(f"\n{__name__}=====> \033[92mSettings instance method called\033[0m\n")
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


def get_settings() -> Settings:
    environment = os.getenv("ENVIRONMENT")

    if not environment:
        raise ValueError("set ENVIRONMENT to 'development' or 'production'")

    return Settings.instance()
