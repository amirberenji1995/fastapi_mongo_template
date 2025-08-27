from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):
    db_address: str
    db_name: str
    app_name: str = "FastAPI"
    app_version: str = "0.1.0"

    # Load env file from ENV_FILE variable, default to .env
    env_file: str = os.environ.get("ENV_FILE", ".env")
    model_config = SettingsConfigDict(env_file=env_file, env_file_encoding="utf-8")


settings = Settings()
