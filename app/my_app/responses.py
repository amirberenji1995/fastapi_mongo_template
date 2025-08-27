from app.base_response import BaseResponse
from app.my_app.schemas import UserRetrieveSchema


class UserCreateResponse(BaseResponse):
    def __init__(
        self,
        data: UserRetrieveSchema,
        message: str = "User created successfully.",
    ):
        super().__init__(message=message, data=data)


class UserRetrieveResponse(BaseResponse):
    def __init__(
        self,
        data: UserRetrieveSchema,
        message: str = "User retrieved successfully.",
    ):
        super().__init__(message=message, data=data)


class UsersListResponse(BaseResponse):
    total: int

    def __init__(
        self,
        data: list[UserRetrieveSchema],
        message: str = "Users list retrieved successfully.",
        total: int = 0,
    ):
        super().__init__(message=message, data=data, total=total)


class UserDeleteResponse(BaseResponse):
    def __init__(
        self,
        data=None,
        message: str = "User deleted successfully.",
    ):
        super().__init__(message=message, data=data)


class UserUpdateResponse(BaseResponse):
    def __init__(
        self,
        data: UserRetrieveSchema,
        message: str = "User updated successfully.",
    ):
        super().__init__(message=message, data=data)
