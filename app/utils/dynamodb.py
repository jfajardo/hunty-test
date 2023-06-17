import uuid

import boto3
from pydantic.class_validators import List

dynamodb = boto3.client('dynamodb')
dynamodb_resource = boto3.resource('dynamodb')


def save_message_to_dynamodb(data):
    """
    Guarda los datos en una tabla de DynamoDB.

    Args:
        data (dict): Los datos a guardar en DynamoDB.

    """
    try:
        table_name = 'hunty_messages'

        # Guarda los datos en la tabla de DynamoDB
        dynamodb.put_item(
            TableName=table_name,
            Item={
                'id': {'S': str(uuid.uuid4())},
                'chat_id': {'N': str(data['chat_id'])},
                'full_name': {'S': data['full_name']},
                'message': {'S': data['message']},
                'reply': {'S': data['reply']},
                'timestamp': {'N': str(data['timestamp'])},
                'user_id': {'N': str(data['user_id'])}
            }
        )

        print('Datos guardados en DynamoDB')

    except Exception as e:
        print('Error al guardar los datos en DynamoDB:', str(e))


def get_records(table_name: str) -> List[dict]:
    """
    Obtiene registros de una tabla de DynamoDB de forma paginada.

    Args:
        table_name (str): El nombre de la tabla de DynamoDB.

    Returns:
        List[dict]: Una lista de registros de DynamoDB.

    """
    table = dynamodb_resource.Table(table_name)
    items = []

    response = table.scan()

    items.extend(response['Items'])
    last_evaluated_key = response.get('LastEvaluatedKey')

    while last_evaluated_key:
        response = table.scan(ExclusiveStartKey=last_evaluated_key)

        items.extend(response['Items'])
        last_evaluated_key = response.get('LastEvaluatedKey')

    return items
