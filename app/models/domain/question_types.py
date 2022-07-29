from pydantic import BaseModel, Field


class Type(BaseModel):
    type: str = Field(None)
