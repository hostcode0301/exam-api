from db import initialize_client

client = initialize_client()

# Create DB table
client.create_table(
    TableName="dev.exam",
    KeySchema=[
        {
            'AttributeName': 'PK',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'SK',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'PK',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'SK',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'GSI1PK',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'GSI1SK',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'GSI2PK',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'GSI2SK',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    },
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'GSI1',
            'KeySchema': [
                {
                    'AttributeName': 'GSI1PK',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'GSI1SK',
                    'KeyType': 'RANGE'
                }
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        },
        {
            'IndexName': 'GSI2',
            'KeySchema': [
                {
                    'AttributeName': 'GSI2PK',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'GSI2SK',
                    'KeyType': 'RANGE'
                }
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        }
    ],
)
