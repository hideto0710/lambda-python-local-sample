import boto3

dynamodb = boto3.resource('dynamodb',
                          region_name='us-east-1',
                          endpoint_url='http://localstack:4569')


def handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print(context)
    print(bucket, key)


def get(event, context):
    return {'statusCode': 200, 'body': 'hello', 'headers': {'X-Custom-Header': 'sample'}}


def create(event, context):
    table = dynamodb.create_table(
        TableName='users',
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return 1
