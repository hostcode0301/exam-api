from typing import List
from fastapi import HTTPException
from app.db.entities.user_tests import UserTest
from app.models.schemas import (
    tests as _test_schemas,
    user_tests as _user_test_schemas,
)
from app.db.data.test.get_user_tests import get_user_tests
from app.db.data.test.update_test_times import update_test_times
from app.db.data.test.create_test import create_test
from app.db.data.test.get_test_by_id import get_test_by_id
from app.db.data.test.take_test import take_test
from app.db.data.user.get_user_by_id import get_user_by_id
from app.utils import (
    test_helpers as _test_helpers,
)


class TestService():
    def create_test(self, test_in: _test_schemas.TestInCreate) -> _test_schemas.TestInResponse:
        test_db = _test_helpers.get_test_dbmodel(test_in)

        _ = create_test(test_db)

        return _test_schemas.TestInResponse(**test_db.dict())

    def take_test(self, user_test_in: _user_test_schemas.UserTestInCreate) -> _user_test_schemas.UserTestInResponse:
        user_db = get_user_by_id(user_test_in.user_id)

        if user_db is None:
            raise HTTPException(status_code=404, detail="User not found")

        test_db = get_test_by_id(user_test_in.test_id)

        if test_db is None:
            raise HTTPException(status_code=404, detail="Test not found")

        existed_user_tests = get_user_tests(user_test_in.user_id)

        if existed_user_tests is not None:
            user_test_db = update_test_times(user_test_in.user_id, user_test_in.test_id)

        
            return _user_test_schemas.UserTestInResponse(UserTest(**user_test_db).dict())
        
        user_test_db = _test_helpers.get_uset_test_dbmodel(test_db, user_db)

        _ = take_test(user_test_db)

        return _user_test_schemas.UserTestInResponse(**user_test_db.dict())

    def get_user_tests(self, user_id: str) -> List[_user_test_schemas.UserTestInResponse]:
        user_tests = get_user_tests(user_id)

        if user_tests is None:
            raise HTTPException(status_code=404, detail="User not found")

        return [_user_test_schemas.UserTestInResponse(**user_test.dict()) for user_test in user_tests]
