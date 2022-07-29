from pydantic import BaseModel, Field


class AnswerText(BaseModel):
    answer_text: str = Field(...)

class AnserImage(BaseModel):
    answer_image: str = Field(None)

class IsCorrectAnswer(BaseModel):
    is_correct_answer: bool = Field(...)