import os, re
import google.generativeai as genai

genai.configure(api_key = os.getenv('GEMINI_API_KEY'))

def contar_tokens(texto):
    # Encuentra todas las palabras (secuencias de caracteres alfanuméricos)
    tokens = re.findall(r'\w+', texto)
    return len(tokens)

def send_prompt_gemini(text):
    model = genai.GenerativeModel('gemini-pro')
    prompt = "Eres un asistente que responde preguntas en base a dos parametros: pregunta y fuente, no puedes responder mas alla de los datos proprocionados en el parametro fuente. "
    prompt += text
    answer = model.generate_content(prompt)
    print('----------------------RESPUESTA GEMINI!!------------------------')
    print(answer.text)
    print('----------------------FIN GEMINI!!------------------------')
    return answer.text, contar_tokens(prompt), contar_tokens(answer.text)

def get_embedding_gemini(text):
    model = 'models/embedding-001'
    return genai.embed_content(model=model,
                                content=text,
                                task_type="retrieval_document")["embedding"]