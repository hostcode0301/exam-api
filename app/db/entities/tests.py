from app.db.entities.base import BaseEntity
from app.models.domain.dbmodel import DBModel
from app.models.domain.tests import TestName
from app.models.schemas.tests import TestEntity


class Test(
    DBModel,
    BaseEntity,
    TestEntity,
):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.pk = Test.get_pk(self.id)
        self.sk = Test.get_sk(self.id)
        self.item_type = "Test"

    @staticmethod
    def get_pk(test_id: str) -> str:
        pk = f"TEST#{test_id}"
        return pk

    @staticmethod
    def get_sk(test_id: str) -> str:
        sk = f"TEST#{test_id}"
        return sk
    
    @staticmethod
    def get_test_pk_and_sk(test_id: str) -> tuple:
        pk = Test.get_pk(test_id)
        sk = Test.get_sk(test_id)
        return pk, sk
