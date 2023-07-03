import openai
from pydantic import BaseModel


class Document(BaseModel):
    prompt: str = ''


def inference(prompt: str) -> list:
    openai.organization = 'org-FlF7DjfN8kf6smfJafiv4p82'
    openai.api_key = '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'
    print('[PROCESANDO]'.center(40, '-'))

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Calculame el factorial 10, cada numero ingresado, calcula el factorial,"
                                          "y si es un texto que me presente error"
                                          ""
                                          ""},
            {"role": "user", "content": prompt},


        ],
        temperature=0
    )

    content = completion.choices[0].message['content']
    total_tokens = completion.usage.total_tokens

    print('[SE TERMINÓ DE PROCESAR]'.center(40, '-'))
    return [content, total_tokens]
