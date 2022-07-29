from datetime import datetime
from pydantic import BaseModel, Field


class DateTimeModelMixin(BaseModel):
    """Mixin for datetime fields."""

    created_at: str = Field(datetime.now().isoformat(' '))
    updated_at: str = Field(datetime.now().isoformat(' '))

    def get_exclude(self):
        attributes = set()
        for attribute, value in self.__dict__.items():
            if isinstance(value, bool) or isinstance(value, int):
                continue
            if not value:
                attributes.add(attribute)
        return attributes

class IDModelMixin(BaseModel):
    """Mixin for id fields."""

    id: str = Field(None)

class PrimaryKeyModelMixin(BaseModel):
    """DynamoDB primary key mixin."""

    pk: str = Field(None, alias="PK")
    sk: str = Field(None, alias="SK")
