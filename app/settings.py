from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI-MongoDB Template"
    app_version: str = "0.0.1"
    db_address: str
    db_name: str

    class Config:
        env_file = ".env"


settings = Settings()
