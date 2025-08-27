from pydantic import BaseModel, Field
from beanie import Document
from datetime import datetime
from uuid6 import uuid7


class BaseUser(BaseModel):
    user_name: str
    phone: str
    email: str
    occupation: str


class User(Document, BaseUser):
    uid: str = Field(default_factory=lambda: str(uuid7()))
    created_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "users"
        indexes = ["uid", "user_name", [("created_at", -1)]]
