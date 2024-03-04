import pdfplumber

def extraer_parrafos(pdf_path):
    parrafos = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Dividir el texto en párrafos basados en saltos de línea
            parrafos.extend(page.extract_text().split('\n\n'))  # Ajusta el separador según tus necesidades
    return parrafos

# Imprimir los párrafos extraídos
#for i, parrafo in enumerate(parrafos_extraidos):
#    print(f'Párrafo {i + 1}: {parrafo}')