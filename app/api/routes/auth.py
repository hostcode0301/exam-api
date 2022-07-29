from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.utils.jwt_helpers import (
    create_access_token,
    get_current_user,
)
from app.models.schemas.auth import AuthIn, AuthOut


router = APIRouter()

@router.post(
    "/login",
)
def login(auth_in: OAuth2PasswordRequestForm = Depends()):
    if auth_in.username == "admin" and auth_in.password == "admin":
        return AuthOut(**{
            "access_token": create_access_token(subject=auth_in.username),
        })

    return {
        "error": "Invalid username or password",
    }

@router.get(
    "/me",
)
def get_me(user: str = Depends(get_current_user)):
    return {
        "username": user,
    }