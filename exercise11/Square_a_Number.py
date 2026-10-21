import json

def lambda_handler(event, context):
    num = event.get('num', 3)
    sqaure = (num ** 2)
    return {
        'statusCode': 200,
        'body': f'the aqaure number of {num} is: {sqaure}'
    }