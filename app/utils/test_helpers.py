import imp
from app.models.schemas import tests as  _test_schemas
from app.utils import helpers as _helpers
from app.db.entities.tests import Test
from app.db.entities.users import User
from app.db.entities.user_tests import UserTest


def get_test_dbmodel(
    test_in: _test_schemas.TestInCreate
) -> Test:
    test_id = _helpers.generate_ksuid()
    pk, sk = Test.get_test_pk_and_sk(test_id)

    test_db = Test(
        **test_in.dict(),
        **{
            "id": test_id,
            "pk": pk,
            "sk": sk,
        }
    )

    return test_db  

def get_uset_test_dbmodel(
    test_db: Test,
    user_db: User
) -> UserTest:
    pk, sk = UserTest.get_user_test_pk_and_sk(user_db.id, test_db.id)

    user_test_db = UserTest(
        **{
            "pk": pk,
            "sk": sk,
            "times": 0,
            "test_name": test_db.test_name,
        }
    )

    return user_test_db
