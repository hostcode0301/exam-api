from app.utils.aws.dynamodb import _dynamodb_resource
from app.db.entities.tests import Test as _TestEntity


def get_test_by_id(test_id: str) -> _TestEntity:
    try:
        pk = _TestEntity.get_pk(test_id)
        sk = _TestEntity.get_sk(test_id)
        rs = _dynamodb_resource.query(
            KeyConditionExpression="PK = :pk AND SK = :sk",
            ExpressionAttributeValues={
                ":pk": pk,
                ":sk": sk,
            },
        )

        return _TestEntity(**rs["Items"][0])
    except Exception as e:
        return None