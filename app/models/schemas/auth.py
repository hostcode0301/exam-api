from pydantic import Field

from app.models.domain import (
    rwmodel as _rwmodel,
)

class AuthIn(
    _rwmodel.BaseModel,
):
    username: str = Field(None)
    password: str = Field(None)

class AuthOut(
    _rwmodel.BaseModel,
):
    access_token: str = Field(None)
