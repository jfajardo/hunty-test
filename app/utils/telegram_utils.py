import requests

from app.utils.constants import TELEGRAM_URL_API, TELEGRAM_TOKEN, APP_URL


def send_telegram_message(chat_id: str, text: str, token: str) -> None:
    """
    Envía un mensaje de texto a través de la API de Telegram.

    Args:
        chat_id (str): El ID del chat o destinatario del mensaje.
        text (str): El texto del mensaje a enviar.
        token (str): El token de autenticación de la API de Telegram.

    Raises:
        requests.HTTPError: Si ocurre un error al realizar la solicitud HTTP.

    """
    try:
        url = f"{TELEGRAM_URL_API}/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": text}
        response = requests.post(url, json=data)
        response.raise_for_status()
    except requests.HTTPError as e:
        raise requests.HTTPError(f"Error al enviar el mensaje de Telegram: {str(e)}")


def set_telegram_webhook() -> None:
    """
    Configura el webhook de Telegram para recibir actualizaciones de mensajes.

    Raises:
        requests.HTTPError: Si ocurre un error al realizar la solicitud HTTP.

    """
    try:
        url = f"{TELEGRAM_URL_API}/bot{TELEGRAM_TOKEN}/setWebhook?url={APP_URL}/messages/"
        response = requests.request("GET", url, headers={}, data={}).json()
        print(f'✅ Setting webhook: {response["description"]}')
    except requests.HTTPError as e:
        raise requests.HTTPError(f"Error al configurar el webhook de Telegram: {str(e)}")
