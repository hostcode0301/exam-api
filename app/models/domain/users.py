from typing import Optional
from pydantic import BaseModel, Field, validator

class Id(BaseModel):
    id: str = Field(None)

class Fullname(BaseModel):
    fullname: str = Field(...)

class OptionalFullname(BaseModel):
    fullname: Optional[str]

class DateOfBirth(BaseModel):
    date_of_birth: str = Field(...)

class OptionalDateOfBirth(BaseModel):
    date_of_birth: Optional[str]

class Address(BaseModel):
    address: str = Field(...)

class OptionalAddress(BaseModel):
    address: Optional[str]

