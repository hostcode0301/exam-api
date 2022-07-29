from pydantic import BaseModel, Field


class Mark(BaseModel):
    mark: float = Field(...)

class IsCorrect(BaseModel):
    is_correct: bool = Field(...)