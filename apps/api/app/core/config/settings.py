from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings, populated from environment variables / .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="GREENHOODSPACE_",
        extra="ignore",
    )

    APP_NAME: str = "greenhoodspace_api"
    APP_DESCRIPTION: str = "An Universal api that provides different protective and clean services for smooth performance and run of GreenHoodSpace."
    APP_VERSION: str = "0.1.0"
    APP_ENVIRONMENT: str

    SERVER_NAME: str = "greenhoodspace"
    SERVER_PATH: str = "app.main:app"
    SERVER_HOST: str = "127.0.0.1"
    SERVER_PORT: int = 8000
    SERVER_RELOAD: bool = True
    SERVER_BASE_API: str = "/api/v1"

    DATABASE_LOCAL_NAME: str
    DATABASE_LOCAL_URL: str
    DATABASE_PRODUCTION_NAME: str
    DATABASE_PRODUCTION_URL: str
    DATABASE_AUTO_COMMIT: bool
    DATABASE_AUTO_FLUSH: bool
    DATABASE_ECHO_LOGS: bool

    @property
    def switch_db_using_env(self) -> str:
        if self.APP_ENVIRONMENT == "dev":
            return self.DATABASE_LOCAL_URL

        elif self.APP_ENVIRONMENT == "prod":
            return self.DATABASE_PRODUCTION_URL

        raise ValueError(
            f"Invalid APP_ENVIRONMENT: {self.APP_ENVIRONMENT!r}. "
            "Expected 'dev' or 'prod'."
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore


APP_SETTINGS = get_settings()
