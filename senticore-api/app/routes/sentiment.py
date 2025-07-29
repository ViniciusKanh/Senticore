# app/routes/sentiment.py

from fastapi import APIRouter
from pydantic import BaseModel
from transformers import pipeline

# ✅ Carrega o pipeline do modelo treinado no Hugging Face
modeloHF = "ViniciusKhan/bert-nps-feedback-analyzer"
sentiment_pipeline = pipeline("text-classification", model=modeloHF)

# ✅ Instancia o roteador
router = APIRouter()

# 📥 Modelo de entrada
class TextoEntrada(BaseModel):
    texto: str

# 🧠 Função principal de inferência
def analisar_sentimento(texto):
    resultado = sentiment_pipeline([texto[:512]])[0]
    sentimento = resultado["label"]  # 'Positive', 'Neutral' ou 'Negative'
    confianca = round(resultado["score"], 4)
    return sentimento, confianca

# 🔄 Lote de textos (opcional)
def analisar_sentimentos_lote(textos, batch_size: int = 16):
    resultados_raw = sentiment_pipeline(
        [t[:512] for t in textos], batch_size=batch_size, truncation=True
    )
    resultados_processados = []
    for res in resultados_raw:
        sentimento = res["label"]
        confianca = round(res["score"], 4)
        resultados_processados.append((sentimento, confianca))
    return resultados_processados

# 🚀 Endpoint principal
@router.post("/analise")
def analise_sentimento(entrada: TextoEntrada):
    sentimento, confianca = analisar_sentimento(entrada.texto)
    return {
        "sentimento": sentimento,
        "confianca": confianca
    }
