from pydantic import BaseModel, Field


class QuestionTitle(BaseModel):
    question_title: str = Field(...)

class QuestionText(BaseModel):
    question_text: str = Field(...)

class QuestionImage(BaseModel):
    question_image: str = Field(None)

class Tips(BaseModel):
    tips: str = Field(None)
