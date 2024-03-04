import os
from openai import OpenAI #importa la libería de OpenAI

#Configuramos nuestra clave  de API de OpenAI
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

def send_prompt_gpt(text):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
            {"role": "system", "content": "Eres un asistente que responde preguntas en base a dos parametros: pregunta y fuente, no puedes responder mas alla de los datos proprocionados en el parametro fuente."},
            {"role": "user", "content": text}
        ]
    )
    print('----------------------RESPUESTA GPT!!------------------------')
    print(response)
    print('----------------------FIN GPT!!------------------------')

    return response.choices[0].message.content,response.usage.prompt_tokens,response.usage.completion_tokens

def get_embedding_gpt(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )

    return response.data[0].embedding