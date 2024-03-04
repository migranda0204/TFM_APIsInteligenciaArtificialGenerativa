from gpt import send_prompt_gpt, get_embedding_gpt
from gemini import send_prompt_gemini, get_embedding_gemini
from extraer_pdf import extraer_parrafos
from chroma import create_collection, save_data, get_collection, get_document, list_collections, get_length_collecion
import pandas as pd

def analizar_prompt_gpt(prompt):
    resultText, useTokensPrompt, useTokensCompletion = send_prompt_gpt(prompt)
    return resultText, useTokensPrompt, useTokensCompletion

def analizar_prompt_gemini(prompt):
    resultText, useTokensPrompt, useTokensCompletion = send_prompt_gemini(prompt)
    return resultText, useTokensPrompt, useTokensCompletion

def obtener_datos_archivo():
    # Ruta al archivo PDF
    ruta_archivo_pdf = 'KOF_Estados_Financieros-2020_Final.pdf'
    parrafos_extraidos = extraer_parrafos(ruta_archivo_pdf)
    return parrafos_extraidos

def generar_datos_gpt():
    parrafos_extraidos = obtener_datos_archivo()
    data = []
    count = 1
    for i in parrafos_extraidos:
        data.append(
            {
                "Id": count,
                "Text": i,
                "TextVector": get_embedding_gpt(i)
            }
        )
        count += 1

    dfVectorGPT = pd.DataFrame(data)
    collection_name = 'CollectionGPT'
    collection = create_collection(collection_name)
    save_data(dfVectorGPT, collection, collection_name)

    return len(dfVectorGPT)

def generar_datos_gemini():
    parrafos_extraidos = obtener_datos_archivo()
    data = []
    count = 1
    for i in parrafos_extraidos:
        data.append(
            {
                "Id": count,
                "Text": i,
                "TextVector": get_embedding_gemini(i)
            }
        )
        count += 1

    dfVectorGemini = pd.DataFrame(data)
    collection_name = 'CollectionGemini'
    collection = create_collection(collection_name)
    save_data(dfVectorGemini, collection, collection_name)

    return len(dfVectorGemini)

def recupera_embedding_gpt(prompt):
    collection_name = 'CollectionGPT'
    collection = get_collection(collection_name)
    documents = get_document(collection, get_embedding_gpt(prompt))
    return documents

def recupera_embedding_gemini(prompt):
    collection_name = 'CollectionGemini'
    collection = get_collection(collection_name)
    documents = get_document(collection, get_embedding_gemini(prompt))
    return documents

def lista_colecciones():
    return list_collections()

def conteo_contenedor():
    collection_name = 'CollectionGPT'
    length_documents = get_length_collecion(collection_name)
    return length_documents

def responde_prompt_gpt(prompt):
    documents = recupera_embedding_gpt(prompt)
    mejor_coincidencia = documents['text'].iloc[0]
    print('----------------------MEJOR COINCIDENCIA GPT!!------------------------')
    print(mejor_coincidencia)
    print('----------------------FIN COINCIDENCIA GPT!!------------------------')
    promptFinal = 'pregunta: ' + prompt + ' '
    promptFinal += 'fuente: ' + mejor_coincidencia
    resultText, useTokensPrompt, useTokensCompletion = analizar_prompt_gpt(promptFinal)
    return resultText, useTokensPrompt, useTokensCompletion

def responde_prompt_gemini(prompt):
    documents = recupera_embedding_gemini(prompt)
    mejor_coincidencia = documents['text'].iloc[0]
    print('----------------------MEJOR COINCIDENCIA GEMINI!!------------------------')
    print(mejor_coincidencia)
    print('----------------------FIN COINCIDENCIA GEMINI!!------------------------')
    promptFinal = 'pregunta: ' + prompt + ' '
    promptFinal += 'fuente: ' + mejor_coincidencia
    resultText, useTokensPrompt, useTokensCompletion = analizar_prompt_gemini(promptFinal)
    return resultText, useTokensPrompt, useTokensCompletion

