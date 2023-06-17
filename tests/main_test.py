import unittest

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


sample_payload = {'update_id': 681910425, 'message': {'message_id': 93, 'from': {'id': 22893231, 'is_bot': False, 'first_name': 'Jonhatan', 'last_name': 'Fajardo', 'username': 'jfajardo', 'language_code': 'en'}, 'chat': {'id': 22893231, 'first_name': 'Jonhatan', 'last_name': 'Fajardo', 'username': 'jfajardo', 'type': 'private'}, 'date': 1686890208, 'text': 'Hola'}}


class TestApp(unittest.TestCase):
    def test_handle_messages(self):
        response = client.post("/messages", json=sample_payload)
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    def test_get_messages(self):
        response = client.get("/messages")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    # Prueba de integración que cubre tanto la función handle_messages como get_messages
    def test_integration(self):
        # Enviar un mensaje
        response = client.post("/messages", json=sample_payload)
        assert response.status_code == 200

        # Obtener los mensajes
        response = client.get("/messages")
        assert response.status_code == 200
