from msilib.schema import Condition
from app.utils.aws.dynamodb import _dynamodb_resource

def update_item(
    pk: str, sk: str,
    update_expression: str, expression_attribute_values: dict,
    return_values: str = "ALL_NEW",
) -> dict:
    """
    Update an item in DynamoDB.
    """
    response = _dynamodb_resource.update_item(
        Key={
            "PK": pk,
            "SK": sk,
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values,
        ConditionExpression="attribute_exists(PK) AND attribute_exists(SK)",
        ReturnValues=return_values,
    )

    return response