from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env',
        env_file_encoding='utf-8'
    )


class PostgresSettings(Config):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    @property
    def postgres_settings(self) -> dict:
        return {
            'name': self.POSTGRES_DB,
            'user': self.POSTGRES_USER,
            'password': self.POSTGRES_PASSWORD,
            'host': self.POSTGRES_HOST,
            'port': self.POSTGRES_PORT
        }

    @property
    def postgres_async_url(self) -> str:
        return 'postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}'.format(
            **self.postgres_settings
        )

    @property
    def postgres_sync_url(self) -> str:
        return 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(
            **self.postgres_settings
        )


class DefaultSettings(Config):
    PROJECT_NAME: str
    DOCS_URL: str
    OPENAPI_URL: str

    POSTGRES: PostgresSettings = PostgresSettings()

    UVICORN_HOST: str
    UVICORN_PORT: str
