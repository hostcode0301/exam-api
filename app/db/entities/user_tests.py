from app.models.domain.dbmodel import DBModel
from app.db.entities.base import BaseEntity
from app.models.schemas.user_tests import UserTestEntity


class UserTest(
    DBModel,
    BaseEntity,
    UserTestEntity,
):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.item_type = "UserTest"

    @staticmethod
    def get_pk(user_id: str) -> str:
        pk = f"USER#{user_id}"
        return pk

    @staticmethod
    def get_sk(test_id: str) -> str:
        sk = f"TEST#{test_id}"
        return sk

    @staticmethod
    def get_user_test_pk_and_sk(user_id: str, test_id: str) -> tuple:
        pk = UserTest.get_pk(user_id)
        sk = UserTest.get_sk(test_id)
        return pk, sk

