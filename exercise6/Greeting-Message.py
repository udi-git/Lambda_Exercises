import json

def lambda_handler(event, context):
    name = event.get('name', 'udi')
    return {
        'statusCode': 200,
        'body': f'Hello, {name}'
        }
