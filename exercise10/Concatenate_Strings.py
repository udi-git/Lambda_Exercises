import json

def lambda_handler(event, context):
    first_word = event.get('first_word', 'Dev')
    second_word = event.get('second_word', 'Ops')
    return {
        'statusCode': 200,
        'body': f'The Word is: {first_word+second_word}'
    }
