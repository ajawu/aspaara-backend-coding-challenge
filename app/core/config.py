import secrets
from typing import Optional

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    SQLALCHEMY_DATABASE_URI: Optional[str] = "sqlite:///data.db"
    PROJECT_NAME: str = "Aspaara Backend Challenge"

    class Config:
        case_sensitive = True


settings = Settings(SERVER_NAME="Local", SERVER_HOST="http://127.0.0.1/")
