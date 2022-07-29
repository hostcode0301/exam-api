import os
from datetime import timedelta
from typing import Union, Any
from fastapi import Depends, HTTPException
from jose import jwt
from fastapi.security import OAuth2PasswordBearer

from app.utils.helpers import get_utc_now

ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"
SECRET_KEY = os.getenv("SECRET_KEY", "thisisaverysecretkey")

def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    """
    Create an access token.
    :param subject: The subject of the token.
    :param expires_delta: Time to expire the token.
    :return: The access token.
    """

    if expires_delta is not None:
        expires_delta = get_utc_now() + expires_delta
    else:
        expires_delta = get_utc_now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    token = jwt.encode(
        {"sub": str(subject), "exp": expires_delta},
        SECRET_KEY,
        algorithm=ALGORITHM,
    )

    return token

resuable_oauth = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login",
    scheme_name="JWT",
)

def get_current_user(token: str = Depends(resuable_oauth)) -> str:
    """
    Get the current user.
    :param token: The token.
    :return: The user.
    """

    try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[ALGORITHM]
        )
        username: str = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=400, detail="Invalid token")
        
        return username
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))