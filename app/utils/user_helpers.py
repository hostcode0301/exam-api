from app.models.schemas import users as _user_schemas
from app.db.entities.users import User
from app.utils import helpers as _helpers


def get_user_dbmodel(
    user_in: _user_schemas.UserInCreate
) -> User:
    user_id = _helpers.generate_ksuid()
    pk, sk = User.get_user_pk_and_sk(user_id)

    user_db = User(
        **user_in.dict(),
        **{
            "id": user_id,
            "pk": pk,
            "sk": sk,
        }
    )

    return user_db
