from pydantic import BaseModel, Field


class Result(BaseModel):
    result: str = Field(...)

class PublishDate(BaseModel):
    publish_date: str = Field(...)
