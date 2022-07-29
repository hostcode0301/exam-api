from app.utils import helpers
from app.utils import db_helpers as _db_helpers
from app.db.entities.user_tests import UserTest


def update_test_times(user_id: str, test_id: str) -> dict:
    pk = UserTest.get_pk(user_id)
    sk = UserTest.get_sk(test_id)
    updated_at = helpers.get_now_iso()

    update_expression = (
        "SET "
        + "UpdatedAt = :updated_at"
        + ", Times = Times + :times"
    )

    expression_attribute_values = {
        ":updated_at": updated_at,
        ":times": 1,
    }

    rs = _db_helpers.update_item(
        pk=pk,sk=sk,
        update_expression=update_expression,
        expression_attribute_values=expression_attribute_values,
    )

    return rs["Attributes"]