from app.utils.aws.dynamodb import _dynamodb_resource
from app.db.entities import users as _user_entity

def create_user(
    user: _user_entity.User,
) -> bool:
    """Create new user in DynamoDB"""

    _dynamodb_resource.put_item(
        Item=user.dict(by_alias=True)
    )
