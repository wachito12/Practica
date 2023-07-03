import openai
from pydantic import BaseModel


class Document(BaseModel):
    prompt: str = ''


def inference(prompt: str) -> list:
    openai.organization = 'org-FlF7DjfN8kf6smfJafiv4p82'
    openai.api_key = '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'
    print('[PROCESANDO]'.center(40, '-'))

    # Diccionario para mapear letras a números
    letter_to_number = {
        'a': '1',
        'b': '2',
        'c': '3',
        'd': '4',
        'e': '5',
        # Agrega el resto de las letras y números según sea necesario
    }

    # Reem-plaza las letras por numeral en el prompt
    prompt_numbers = ''.join(letter_to_number.get(char.lower(), char) for char in prompt)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Escribe alreves la palabra hola "},
            {"role": "user", "content": prompt_numbers},
            {"role": "assistant", "content": ""}

        ],
        temperature=0
    )

    content = completion.choices[0].message['content']
    total_tokens = completion.usage.total_tokens

    print('[SE TERMINÓ DE PROCESAR]'.center(40, '-'))
    return [content, total_tokens]
