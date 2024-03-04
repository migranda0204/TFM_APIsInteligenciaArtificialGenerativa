<!DOCTYPE html>
<html>

<head>
    <title>Bienvenido al portal empresarial para análisis de datos con Inteligencia Artificial Generativa. </title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
        integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <link rel="stylesheet" href="css/style.css">
</head>

<body>
    <div class="container mt-5">
        <h1>Bienvenido al portal empresarial para análisis de datos con Inteligencia Artificial Generativa.</h1>
        <p>Escribe tu prompt a continuación para obtener el comparativo de respuestas de los modelos GPT 3.5 y Google Gemini Pro.</p>
        <form id="gpt3-form">
            <div class="form-group">
                <label for="prompt">Prompt</label>
                <textarea class="form-control" id="prompt" name="prompt" rows="3"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Obtener respuesta</button>
        </form>
        <div id="gpt3-response" class="mt-3"></div>

<h5>Respuesta de Chat GPT</h5>
<p>.</p>
    <!-- Incluye jQuery y el script que contiene el código de AJAX
	Respuesta de GPT -->
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="js/script_OpenAI.js"></script>
<h5>Respuesta de Google Gemini</h5>
<p>.</p>
   <!-- RESPUESTA DE Google Gemini pro 1.0 -->
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="js/script_Gemini.js"></script>
  </div>
</body>

</html>