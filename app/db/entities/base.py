from pydantic import BaseModel, Field

from app.utils import helpers as _helpers

class BaseEntityUpdatedAt(BaseModel):
    updated_at: str = Field(_helpers.get_now_iso())

class BaseEntityCreatedAt(BaseModel):
    created_at: str = Field(_helpers.get_now_iso())

class ItemType(BaseModel):
    item_type: str = Field(None)

class BaseEntity(
    BaseEntityUpdatedAt,
    BaseEntityCreatedAt,
    ItemType,
):
    pk: str = Field(None, alias="PK")
    sk: str = Field(None, alias="SK")
