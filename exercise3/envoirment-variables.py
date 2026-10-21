import os

def lambda_handler(event, context):
    my_value = os.environ.get('GREETING')
    
    return {
        'statusCode': 200,
        'body': f"The value is: {my_value}"
    }