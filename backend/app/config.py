from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    SUPABASE_URL: str
    SUPABASE_ANON_KEY: str
    SUPABASE_SECRET_KEY: str

    CAREER_BUCKET: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()

APP_NAME = settings.APP_NAME
APP_VERSION = settings.APP_VERSION

SUPABASE_URL = settings.SUPABASE_URL
SUPABASE_ANON_KEY = settings.SUPABASE_ANON_KEY
SUPABASE_SECRET_KEY = settings.SUPABASE_SECRET_KEY

CAREER_BUCKET = settings.CAREER_BUCKET