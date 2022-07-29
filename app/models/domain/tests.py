from pydantic import BaseModel, Field


class Id(BaseModel):
    id: str = Field(...)

class TestName(BaseModel):
    test_name: str = Field(...)