from app.models.schemas.users import UserInUpdate
from app.db.entities.users import User as UserEntity
from app.utils import helpers
from app.utils import db_helpers as _db_helpers

def update_user_profile_info(user_id, user_in: UserInUpdate) -> dict:
    pk = UserEntity.get_pk(user_id)
    sk = UserEntity.get_sk(user_id)
    updated_at = helpers.get_now_iso()

    update_expression = (
        "SET "
        + "UpdatedAt = :updated_at"
        # + ", Fullname = :fullname"
        # + ", Address = :address"
        # + ", DateOfBirth = :date_of_birth"
    )

    expression_attribute_values = {
        ":updated_at": updated_at,
        # ":fullname": user_in.fullname,
        # ":address": user_in.address,
        # ":date_of_birth": user_in.date_of_birth,
    }

    if user_in.fullname is not None:
        update_expression += ", Fullname = :fullname"
        expression_attribute_values[":fullname"] = user_in.fullname
    
    if user_in.address is not None:
        update_expression += ", Address = :address"
        expression_attribute_values[":address"] = user_in.address

    if user_in.date_of_birth is not None:
        update_expression += ", DateOfBirth = :date_of_birth"
        expression_attribute_values[":date_of_birth"] = user_in.date_of_birth

    rs = _db_helpers.update_item(
        pk=pk,sk=sk,
        update_expression=update_expression,
        expression_attribute_values=expression_attribute_values,
    )

    return rs["Attributes"]
