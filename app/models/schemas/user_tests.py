from app.models.domain.rwmodel import RWModel
from app.models.domain.user_tests import Times, TestId, UserId
from app.models.domain.tests import TestName


class UserTestInCreate(
    RWModel,
    TestId,
    UserId,
):
    pass

class UserTestEntity(
    RWModel,
    TestName,
    Times,
):
    pass

class UserTestInResponse(
    UserTestEntity,
):
    pass