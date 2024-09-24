from fastapi import FastAPI
import requests
import pdfplumber
from io import BytesIO

app = FastAPI()

@app.post("/extract-text")
async def extract_text(urlPdf: str):
    # Faz o download do arquivo PDF a partir da URL
    response = requests.get(urlPdf)
    response.raise_for_status()  # Verifica se o download foi bem-sucedido
    
    # Abre o PDF usando o conteúdo baixado
    with pdfplumber.open(BytesIO(response.content)) as pdf:
        text = ""
        # Extrai o texto de cada página
        for page in pdf.pages:
            text += page.extract_text()

    return {"extracted_text": text}
