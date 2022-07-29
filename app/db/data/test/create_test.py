from app.db.entities.tests import Test
from app.utils.aws.dynamodb import _dynamodb_resource


def create_test(
    test: Test,
) -> bool:
    """Create new test in DynamoDB"""

    _dynamodb_resource.put_item(
        Item=test.dict(by_alias=True)
    )
