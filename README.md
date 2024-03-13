# TFM_APIsInteligenciaArtificialGenerativa
Incluye el código desarrollado para preparación e integración de datos con las APIs GPT 3.5 de Open AI y Google Gemini Pro.

El trabajo está estructurado en los siguientes apartados:
o	Requisitos
o	Integración y uso de API GPT 3.5 de Open AI
o	Integración y uso de API Google Gemini Pro 1.0
o	Módulo de Procesamiento de datos
o	Interfaz de usuario

1.	Requisitos: Contienen el listado de librerías y módulos que se utilizan en el desarrollo para realizar tareas como extracción y análisis de datos y generación de contenido.
2.	Integración y uso de API GPT 3.5 de Open AI (gpt.py): Se configura la clave API, se define funciones para enviar prompts a GPT-3.5 y obtener embeddings de texto.
3.	Integración y uso de API Google Gemini Pro 1.0 (gemini.py): Similar a GPT, se configura la clave API de Gemini, se define funciones para enviar prompts a Gemini y obtener embeddings de texto.
4.	Módulo de Procesamiento de datos: extrae los datos de la fuente de datos, genera embeddings y los datos se almacenan en Chroma DB.
5.	Interfaz de usuario (index.html): se crea una interfaz para recibir y enviar propmts a GPT 3.5 y Google GeminiPro. Y se comparan los resultados.

