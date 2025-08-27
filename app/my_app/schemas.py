from app.my_app.models import BaseUser
from datetime import datetime
from typing import ClassVar, Optional
from pydantic import BaseModel, model_validator


class UserCreateSchema(BaseUser):
    is_deleted: ClassVar[None] = None


class UserRetrieveSchema(BaseUser):
    uid: str
    created_at: datetime
    is_deleted: ClassVar[None] = None


class UserUpdateSchema(BaseModel):
    user_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    occupation: Optional[str] = None

    @model_validator(mode="after")
    def check_fields(self):
        if not any(value is not None for value in self.model_dump().values()):
            raise ValueError("At least one field must be provided for update.")
        return self
