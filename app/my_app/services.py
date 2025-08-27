from app.my_app.schemas import UserCreateSchema, UserRetrieveSchema, UserUpdateSchema
from app.my_app.models import User
from app.base_error import NotFoundError


async def create_user_service(payload: UserCreateSchema) -> UserRetrieveSchema:
    user = User(**payload.model_dump())
    await user.insert()

    return UserRetrieveSchema(**user.model_dump())


async def get_user_service(uid: str):
    user = await User.find_one(User.uid == uid)

    if not user:
        raise NotFoundError("User").error

    return UserRetrieveSchema(**user.model_dump())


async def get_user_list_service(offset: int, limit: int):
    total = await User.count()
    user = await User.find().skip(offset).limit(limit).to_list()

    return [UserRetrieveSchema(**user.model_dump()) for user in user], total


async def update_user_service(uid: str, update_payload: UserUpdateSchema):
    user = await User.find_one(User.uid == uid)

    if not user:
        raise NotFoundError("User").error

    await user.set(update_payload.model_dump(exclude_none=True))
    await user.save()

    return UserRetrieveSchema(**user.model_dump())


async def delete_user_service(uid: str):
    user = await User.find_one(User.uid == uid)

    if not user:
        raise NotFoundError("User").error

    await user.delete()
