from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DB_")

    PORT: int
    HOST: str
    DATABASE: str
    USERNAME: str
    PASSWORD: str

    @property
    def db_url(self) -> str:
        return f'postgresql+{self.driver}://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}'

    @property
    def driver(self) -> str:
        return 'asyncpg'


class ApplicationSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="APP_")

    DEBUG: bool
