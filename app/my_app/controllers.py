from fastapi import APIRouter, status, Query
from app.my_app.schemas import UserCreateSchema, UserRetrieveSchema, UserUpdateSchema
from app.my_app.services import (
    create_user_service,
    get_user_service,
    get_user_list_service,
    update_user_service,
    delete_user_service,
)

from app.my_app.responses import (
    UserCreateResponse,
    UserRetrieveResponse,
    UsersListResponse,
    UserUpdateResponse,
    UserDeleteResponse,
)
from app.base_error import NotFoundError

router = APIRouter(prefix="/my_app", tags=["my_app"])


@router.post(
    "/users",
    response_model=UserCreateResponse[UserRetrieveSchema],
    status_code=status.HTTP_201_CREATED,
)
async def create_user(payload: UserCreateSchema):
    """Simple create endpoint."""
    user: UserRetrieveSchema = await create_user_service(payload)

    return UserCreateResponse(user)


@router.get(
    "/users/{uid}",
    response_model=UserRetrieveResponse[UserRetrieveSchema],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "content": {"application/json": {"example": NotFoundError("User").example}},
        }
    },
)
async def get_user_by_uid(uid: str):
    """Simple get by uid endpoint."""
    user: UserRetrieveSchema = await get_user_service(uid)

    return UserRetrieveResponse(user)


@router.get(
    "/users/",
    response_model=UsersListResponse[list[UserRetrieveSchema]],
    status_code=status.HTTP_200_OK,
)
async def get_users_list(
    offset: int = Query(default=0, ge=0), limit: int = Query(default=10, ge=0, le=100)
):
    users_list, total = await get_user_list_service(offset, limit)

    return UsersListResponse(data=users_list, total=total)


@router.delete(
    "/users/{uid}",
    response_model=UserDeleteResponse[UserRetrieveSchema],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "content": {"application/json": {"example": NotFoundError("User").example}},
        }
    },
)
async def delete_user_by_uid(uid: str):
    await delete_user_service(uid)

    return UserDeleteResponse()


@router.put(
    "/users/{uid}",
    response_model=UserUpdateResponse[UserRetrieveSchema],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "content": {"application/json": {"example": NotFoundError("User").example}},
        }
    },
)
async def update_user_by_uid(uid: str, update_payload: UserUpdateSchema):
    user: UserRetrieveSchema = await update_user_service(uid, update_payload)

    return UserUpdateResponse(user)
