def lambda_handler(event, context):
    original_string = event.get('string','DevOps')
    reversed_string = original_string[ ::- 1]
    return {
    'statusCode': 200,
    'body': f'The reverse of the word: {original_string} = {reversed_string}.'
    }