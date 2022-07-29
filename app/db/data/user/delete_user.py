from app.db.entities.users import User as UserEntity
from app.utils.aws.dynamodb import _dynamodb_resource

def delete_user(user_id: str) -> bool:
    """Delete user from DynamoDB"""

    pk = UserEntity.get_pk(user_id)
    sk = UserEntity.get_sk(user_id)

    rs = _dynamodb_resource.delete_item(
        Key={
            "PK": pk,
            "SK": sk,
        },
        ConditionExpression="attribute_exists(PK) AND attribute_exists(SK)",
    )

    return True