import json

def lambda_handler(event, context):
    num = int(event.get('num', '5'))
    if num % 2 == 0:
        result = "even"
    else: 
        result = "odd"
    
    return {
        'statusCode': 200,
        'body': f'the number {num} is {result}:'
    }
