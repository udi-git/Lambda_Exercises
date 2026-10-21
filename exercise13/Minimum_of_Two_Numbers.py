import json

def lambda_handler(event, context):
    num1 = event.get('num1', 8)
    num2 = event.get('num2', 4)
    if num1 < num2:
        result = num1
    else:
        result = num2
    return {
        'statusCode': 200,
        'body': f'The Minimum of the numbers {num1} and {num2} is: {result}'
    }
