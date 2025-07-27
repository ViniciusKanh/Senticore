# app/routes/sentiment.py

from fastapi import APIRouter
from pydantic import BaseModel
from transformers import pipeline

# ✅ Carrega o pipeline do Hugging Face
modeloHF = "ViniciusKhan/senticore-bert-sentiment"
sentiment_pipeline = pipeline("sentiment-analysis", model=modeloHF)

# ✅ Criar roteador da API
router = APIRouter()

# 📥 Modelo de entrada
class TextoEntrada(BaseModel):
    texto: str

# 🎯 Função para classificar sentimento com base nas estrelas
def classificar_estrelas(estrela):
    if estrela in [0, 1, 2]:
        return "Negativo"
    elif estrela == 3:
        return "Neutro"
    else:
        return "Positivo"

# 🧠 Função principal de inferência com pipeline
def analisar_sentimento(texto):
    resultado = sentiment_pipeline([texto[:512]])[0]
    estrelas = int(resultado["label"][0])  # Ex: "5 stars" → 5
    sentimento = classificar_estrelas(estrelas - 1)  # Ajusta índice (1–5 → 0–4)
    confianca = round(resultado["score"], 4)
    return sentimento, confianca


# 🔄 Função otimizada para processar vários textos de uma vez
def analisar_sentimentos_lote(textos, batch_size: int = 16):
    resultados_raw = sentiment_pipeline(
        [t[:512] for t in textos], batch_size=batch_size, truncation=True
    )
    resultados_processados = []
    for res in resultados_raw:
        estrelas = int(res["label"][0])
        sentimento = classificar_estrelas(estrelas - 1)
        confianca = round(res["score"], 4)
        resultados_processados.append((sentimento, confianca))
    return resultados_processados

# 🚀 Endpoint da API
@router.post("/analise")
def analise_sentimento(entrada: TextoEntrada):
    sentimento, confianca = analisar_sentimento(entrada.texto)
    return {
        "sentimento": sentimento,
        "confianca": confianca
    }
