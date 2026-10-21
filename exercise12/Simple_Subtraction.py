import json

def lambda_handler(event, context):
    num1 = event.get('num1', 5)
    num2 = event.get('num2', 4)
    result = (num1 - num2)
    return {
        'statusCode': 200,
        'body': f'The subtraction of {num1}-{num2} is : {result}'
    }