from datetime import datetime
from typing import List

from fastapi import APIRouter, Body
from starlette.responses import JSONResponse

from app.utils.dynamodb import save_message_to_dynamodb, get_records
from app.utils.gpt3 import get_response
from app.utils.telegram_utils import send_telegram_message
from app.utils.constants import TELEGRAM_TOKEN

router = APIRouter()


@router.post("/")
def handle_messages(payload: dict = Body(...)):
    """
    Maneja los mensajes recibidos desde Telegram, recibe el mensaje y lo envía al API de OpenAI, y guardar un registros
    en DynamoDB

    Args:
        payload (Dict[str, dict]): El payload recibido desde Telegram.

    Returns:
        Dict[str, str]: Un diccionario con el estado de la respuesta.

    """
    try:
        chat_id = payload['message']['chat']['id']
        message = payload['message']['text']
        user_id = payload['message']['from']['id']
        full_name = f"{payload['message']['from']['first_name']} {payload['message']['from']['last_name']}"

        if message == '/start':
            message = f'Dale un mensaje bien de bienvenida a {full_name}'
        text_response = get_response(message)
        # text_response = message
        data = {
            'timestamp': int(datetime.now().timestamp()),
            'chat_id': chat_id,
            'message': message,
            'user_id': user_id,
            'full_name': full_name,
            'reply': text_response
        }
        send_telegram_message(chat_id, text_response, TELEGRAM_TOKEN)
        save_message_to_dynamodb(data)
        return {'status': 'ok'}
    except Exception as ex:
        error_message = str(ex)
        return JSONResponse(status_code=500, content={'status': 'error', 'error': error_message})


@router.get("/")
def get_messages() -> List[dict]:
    """
    Obtiene todos los registros de una tabla de DynamoDB paginados.

    Returns:
        List[dict]: Una lista de registros de DynamoDB.

    """
    table_name = 'hunty_messages'
    records = get_records(table_name=table_name)
    return records
