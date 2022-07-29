from app.models.domain.dbmodel import DBModel
from app.models.schemas import users as _user_schemas
from app.db.entities.base import BaseEntity

class User(
    DBModel,
    BaseEntity,
    _user_schemas.UserEntity,
):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.pk = User.get_pk(self.id)
        self.sk = User.get_sk(self.id)
        self.item_type = "User"
    
    @staticmethod
    def get_pk(user_id: str) -> str:
        pk = f"USER#{user_id}"
        return pk

    @staticmethod
    def get_sk(user_id: str) -> str:
        sk = f"USER#{user_id}"
        return sk

    @staticmethod
    def get_user_pk_and_sk(user_id: str) -> tuple:
        pk = User.get_pk(user_id)
        sk = User.get_sk(user_id)
        return pk, sk
