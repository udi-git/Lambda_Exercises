import json

def lambda_handler(event, context):
    word = event.get('word', 'hello')
    length = len(word)
    return {
        'statusCode': 200,
        'body': f'The Length of the ({word}) is: {length}'
        }
