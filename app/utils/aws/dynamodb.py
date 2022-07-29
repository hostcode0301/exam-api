import boto3
from app.core.config import config

_dynamodb_client = boto3.client(
    'dynamodb', 
    endpoint_url=config.dynamodb_enpoint_url,
)

_dynamodb_resource = boto3.resource(
    'dynamodb',
    endpoint_url=config.dynamodb_enpoint_url,
).Table(config.dynamodb_tbl)
