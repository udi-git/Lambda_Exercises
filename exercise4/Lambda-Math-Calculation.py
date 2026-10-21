def lambda_handler(event, context):
    num1 = int(event.get('num1',5))
    num2 = int(event.get('num2',8))
    sum_result = num1 + num2
    return {
    'statusCode': 200,
    'body': f'The sum of {num1} and {num2} is {sum_result}.'
    }
