import json
import boto3
import os


# Initialize dynamodb boto3 object
dynamodb = boto3.resource('dynamodb')
# Set dynamodb table name variable from env
#ddbTableName = os.environ['databaseName']
ddbTableName = 'websiteCounter'
table = dynamodb.Table(ddbTableName)


def lambda_handler(event, context):
    # Update item in table or add if doesn't exist
    ddbResponse = table.update_item(
        Key={
            'id': 'counter'
        },
        UpdateExpression='SET visitorCount = visitorCount + :value',
        ExpressionAttributeValues={
            ':value':1
        },
        ReturnValues="UPDATED_NEW"
    )


    # Format dynamodb response into variable
    responseBody = json.dumps({"count": int(ddbResponse["Attributes"]["visitorCount"])})


    # Create api response object
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        "body": responseBody
    }


    # Return api response object

    return apiResponse
