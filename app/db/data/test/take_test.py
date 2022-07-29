from app.db.entities.user_tests import UserTest
from app.utils.aws.dynamodb import _dynamodb_resource


def take_test(
    user_test: UserTest
):
    _dynamodb_resource.put_item(
        Item=user_test.dict(by_alias=True)
    )
