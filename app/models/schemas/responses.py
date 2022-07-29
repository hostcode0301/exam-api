from pydantic import Field
from app.models.domain.rwmodel import RWModel


class ResponseModel(
    RWModel,
):
    code: int = Field(..., description="Response code")
    message: str = Field(..., description="Response message")