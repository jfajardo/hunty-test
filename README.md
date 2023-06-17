## Descripción del Proyecto

El proyecto es una API desarrollada con FastAPI que se encarga de manejar los mensajes recibidos desde Telegram. La API utiliza el API de OpenAI para generar respuestas a los mensajes y guarda los registros en DynamoDB.

DynamoDB es una opción ideal para esta aplicación debido a su escalabilidad, rendimiento rápido y consistente, alta disponibilidad y durabilidad. Además, su flexibilidad en el esquema de datos y su integración con otros servicios de AWS hacen que sea una elección conveniente para almacenar y gestionar los mensajes de la aplicación de manera eficiente.

La API consta de dos rutas principales:

### Ruta POST ("/messages")

Esta ruta se utiliza para recibir los mensajes desde Telegram. Los mensajes se envían en forma de payload JSON y contienen información como el ID del chat, el texto del mensaje y los datos del remitente. La ruta procesa el mensaje de la siguiente manera:

1. Extrae los datos relevantes del payload, como el ID del chat, el texto del mensaje, el ID del usuario y el nombre completo del remitente.
2. Si el mensaje es "/start", se genera un mensaje de bienvenida personalizado.
3. Llama a la función `get_response` del módulo `app.utils.gpt3` para obtener una respuesta utilizando el API de OpenAI.
4. Crea un diccionario con los datos del mensaje, incluyendo la marca de tiempo, el ID del chat, el texto del mensaje, el ID del usuario, el nombre completo del remitente y la respuesta generada.
5. Llama a la función `send_telegram_message` del módulo `app.utils.telegram_utils` para enviar la respuesta al chat de Telegram.
6. Llama a la función `save_message_to_dynamodb` del módulo `app.utils.dynamodb` para guardar el mensaje en DynamoDB.
7. Retorna un diccionario con el estado de la respuesta, en este caso, {"status": "ok"}.

En caso de que ocurra alguna excepción durante el procesamiento del mensaje, se captura la excepción y se retorna una respuesta de error con el mensaje de error correspondiente.

### Ruta GET ("/messages")

Esta ruta se utiliza para obtener todos los registros de una tabla de DynamoDB de manera paginada. La ruta realiza los siguientes pasos:

1. Define el nombre de la tabla de DynamoDB a partir de la variable `table_name`.
2. Llama a la función `get_records` del módulo `app.utils.dynamodb` para obtener los registros de la tabla especificada.
3. Retorna una lista de registros de DynamoDB.

El proyecto también incluye funciones adicionales en los módulos `app.utils.dynamodb`, `app.utils.gpt3` y `app.utils.telegram_utils` para interactuar con DynamoDB, utilizar el API de OpenAI y enviar mensajes a través de Telegram.

El objetivo principal del proyecto es proporcionar una API que permita recibir mensajes desde Telegram, generar respuestas utilizando el modelo de lenguaje de OpenAI y almacenar los registros en DynamoDB. Además, se ofrece una ruta adicional para consultar los registros almacenados en DynamoDB.

El proyecto se puede configurar y ejecutar en un servidor para que esté disponible como un servicio que maneje y responda a los mensajes recibidos desde Telegram de manera automática.

