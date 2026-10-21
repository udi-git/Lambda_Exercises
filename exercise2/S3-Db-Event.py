import json

def lambda_handler(event, context):
    if event['event'] == 's3':
        return 's3'
    elif event['event'] == 'db':
        return 'db'
    else:
        return "Unknown Service"