from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, jsonify
from funciones import responde_prompt_gpt, responde_prompt_gemini, generar_datos_gpt, generar_datos_gemini , lista_colecciones, conteo_contenedor

app = Flask(__name__)

@app.route('/')
def index():
    return '¡Hola, mundo! Esta es mi aplicación Flask.'

@app.route('/generar_embedding', methods=['GET'])
def generar_embedding():
    rowsGPT = generar_datos_gpt()
    rowsGemini = generar_datos_gemini()
    return f'Se realizó el embedding de: GPT - {rowsGPT} y Gemini {rowsGemini} fila(s).'

@app.route('/obtener_colecciones', methods=['GET'])
def obtener_colecciones():
    colecciones = lista_colecciones()
    return str(colecciones)

@app.route('/obtener_numero_documentos', methods=['GET'])
def obtener_numero_documentos():
    conteo = conteo_contenedor()
    return str(conteo)


@app.route('/recibe_prompt', methods=['POST'])
def recibe_prompt():
    try:
        data = request.get_json()  # Obtener datos en formato JSON
        prompt = data.get('prompt')
        temperatura = data.get('temperatura')
        resultTextGPT, useTokensPromptGPT, useTokensCompletionGPT = responde_prompt_gpt(prompt)
        resultTextGemini, useTokensPromptGemini, useTokensCompletionGemini = responde_prompt_gemini(prompt)
        respuesta = {
            "GPT":{
                "Text":resultTextGPT,
                "TokensPrompt":useTokensPromptGPT,
                "TokensCompletion":useTokensCompletionGPT,
                "TotalTokens": useTokensPromptGPT + useTokensCompletionGPT
            },
            "Gemini":{
                "Text":resultTextGemini,
                "TokensPrompt":useTokensPromptGemini,
                "TokensCompletion":useTokensCompletionGemini,
                "TotalTokens": useTokensPromptGemini + useTokensCompletionGemini
            }
        }

        return respuesta
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
