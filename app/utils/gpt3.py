import openai


def get_response(text: str) -> str:
    """
    Obtiene una respuesta del modelo GPT-3 a partir de un texto de entrada.

    Args:
        text (str): El texto de entrada para generar una respuesta.

    Returns:
        str: La respuesta generada por el modelo.

    Raises:
        OpenAIException: Si hay un error al comunicarse con la API de OpenAI.

    """
    try:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=text,
            max_tokens=1024,
            temperature=0.7,
            n=1,
            stop=None
        )
        return response.choices[0].text.strip().split('\n')[0]
    except openai.OpenAIError as e:
        return f"Error al comunicarse con la API de OpenAI: {str(e)}"

