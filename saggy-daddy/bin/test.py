import boto3

dynamodb = boto3.resource('dynamodb')

table =  dynamodb.Table('discordpy')

table.put_item(
    Item={
        'userid':1234,
    }
)
