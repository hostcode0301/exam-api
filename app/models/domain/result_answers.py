from pydantic import BaseModel, Field


class IsUserChoice(BaseModel):
    is_user_choice: bool = Field(None)