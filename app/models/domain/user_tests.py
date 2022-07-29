from pydantic import BaseModel, Field


class Times(BaseModel):
    times: int = Field(...)

class TestId(BaseModel):
    test_id: str = Field(...)

class UserId(BaseModel):
    user_id: str = Field(...)