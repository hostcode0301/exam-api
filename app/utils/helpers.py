from datetime import datetime
from typing import Optional
from fastapi import HTTPException
import jwt
from ksuid import Ksuid

from app.resources import res_msg


def get_now_iso() -> str:
    now_iso = datetime.now().isoformat(' ')
    return now_iso

def get_utc_now() -> datetime:
    """
    Get the current UTC time.
    """

    return datetime.utcnow()

def generate_ksuid(date: Optional[datetime] = None) -> str:
    """
    Generate a Ksuid which is a unique id also store a date component.
    """
    
    if date is None:
        date = datetime.now()
    kid = str(Ksuid(date))
    return kid

def decode_jwt_token(token: str) -> dict:
    """
    Decode a JWT token.
    """

    try:
        return jwt.decode(
            token.replace("Bearer ", ""),
            options = {
                "verify_signature": False,
            }
        )
    except Exception:
        raise HTTPException(
            status_code=400,
            detail=res_msg.TOKEN_IS_INVALID,
        )