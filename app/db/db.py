import boto3

from boto3.resources.base import ServiceResource

ENDPOINT_URL = 'http://localhost:8000'

def initialize_resource() -> ServiceResource:
    """Create an resource of DynamoDB client."""

    ddb = boto3.resource(
        'dynamodb', 
        endpoint_url = ENDPOINT_URL
    )
    
    return ddb

def initialize_client():
    """Create an instance of the DynamoDB client."""

    client = boto3.client(
        'dynamodb', 
        endpoint_url = ENDPOINT_URL
    )

    return client