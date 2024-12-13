from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DSN: str

"""
Настройки для приложения
"""
settings = Settings()
