from fastapi import HTTPException
from botocore.exceptions import ClientError

from app.models.schemas import (
    users as _user_schema,
)
from app.db.data.user.create_user import create_user
from app.db.data.user.get_user_by_id import get_user_by_id
from app.db.data.user.update_user_profile import update_user_profile_info
from app.db.data.user.delete_user import delete_user
from app.utils import (
    user_helpers as _user_helpers,
    validate_helpers as _validate_helpers,
)

class UserService():
    
    def create_user(self, user_in: _user_schema.UserInCreate) -> _user_schema.UserInResponse:

        _validate_helpers.validate_date_format(user_in.date_of_birth)

        user_db = _user_helpers.get_user_dbmodel(user_in)

        _ = create_user(user_db)

        return _user_schema.UserInResponse(**user_db.dict())

    def get_user_by_id(self, user_id: str) -> _user_schema.UserInResponse:
        user_db = get_user_by_id(user_id)

        if user_db is None:
            raise HTTPException(status_code=404, detail="User not found")

        return _user_schema.UserInResponse(**user_db.dict())

    def update_user(self, user_id: str, user_in: _user_schema.UserInUpdate) -> dict:
        
        res = update_user_profile_info(user_id, user_in)

        return res

    def delete_user(self, user_id: str) -> bool:

        try :
            res = delete_user(user_id)
        except ClientError as e:
            raise HTTPException(status_code=404, detail="User not found")

        return True