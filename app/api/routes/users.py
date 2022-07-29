from fastapi import APIRouter
from app.models.schemas.responses import ResponseModel

from app.models.schemas.users import UserInCreate, UserInResponse, UserInUpdate
from app.services.users import UserService


router = APIRouter()

user_service = UserService()

@router.get(
    "/{user_id}",
    response_model=UserInResponse,
)
def get_user_by_id(user_id: str):

    user = user_service.get_user_by_id(user_id)

    return user

@router.post(
    "",
    response_model=UserInResponse,
)
def create_user(new_user: UserInCreate):

    return user_service.create_user(new_user)

@router.put(
    "/{user_id}",
    response_model=ResponseModel,
)
def update_user(user_id: str, user_in: UserInUpdate):
    
    _ = user_service.update_user(user_id, user_in)

    return ResponseModel(
        code=200,
        message="User updated",
    )

@router.delete(
    "/{user_id}",
    response_model=ResponseModel,
)
def delete_user(user_id: str):
    
    _ = user_service.delete_user(user_id)

    return ResponseModel(
        code=200,
        message="User deleted",
    )