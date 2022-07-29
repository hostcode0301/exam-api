from typing import List

from app.db.entities.user_tests import UserTest as _UserTestEntity
from app.utils.aws.dynamodb import _dynamodb_resource


def get_user_tests(user_id: str) -> List[_UserTestEntity]:
    try:
        pk = _UserTestEntity.get_pk(user_id)
        rs = _dynamodb_resource.query(
            KeyConditionExpression="PK = :pk AND begins_with(SK, :sk)",
            ExpressionAttributeValues={
                ":pk": pk,
                ":sk": "TEST#",
            },
        )

        return [_UserTestEntity(**item) for item in rs["Items"]]
    except Exception as e:
        return None