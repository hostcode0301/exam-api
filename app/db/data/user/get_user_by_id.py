from app.utils.aws.dynamodb import _dynamodb_resource
from app.db.entities.users import User as _UserEntity

def get_user_by_id(user_id: str) -> _UserEntity:
    try:
        pk = _UserEntity.get_pk(user_id)
        sk = _UserEntity.get_sk(user_id)
        rs = _dynamodb_resource.query(
            KeyConditionExpression="PK = :pk AND SK = :sk",
            ExpressionAttributeValues={
                ":pk": pk,
                ":sk": sk,
            },
        )

        return _UserEntity(**rs["Items"][0])
    except Exception as e:
        return None
