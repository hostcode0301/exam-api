from pydantic import BaseModel, Field
from app.models.domain.rwmodel import RWModel
from app.models.domain.tests import TestName, Id

class TestInCreate(
    TestName,
    RWModel
):
    pass

class TestEntity(
    TestInCreate,
    Id,
):
    pass

class TestInResponse(TestEntity):
    pass


class TakeTest(
    RWModel
):
    user_id : str = Field(...)
    test_id : str = Field(...)
