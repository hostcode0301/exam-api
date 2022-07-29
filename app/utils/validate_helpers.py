from fastapi import HTTPException
from datetime import date

from app.resources import res_msg


def validate_date_format(date_str: str) -> None:
    try:
        date.fromisoformat(date_str)
    except (TypeError, ValueError):
        raise_error(400, res_msg.DATE_INVALID_FORMAT)

def raise_error(error_code: int, error_message: str):
    raise HTTPException(
        status_code=error_code,
        detail=error_message,
    )