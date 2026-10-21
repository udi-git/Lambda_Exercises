import json

def lambda_handler(event, context):
    word = event.get('word', 'welcome')
    upper_word = word.upper() 
    return {
        'statusCode': 200,
        'body': f'The UpperCase of the word ({word}) is: {upper_word}!'
    }
