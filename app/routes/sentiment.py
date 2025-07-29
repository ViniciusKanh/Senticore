from fastapi import APIRouter
from pydantic import BaseModel
from transformers import pipeline

# ✅ Nome do modelo no Hugging Face Hub
modeloHF = "ViniciusKhan/bert-nps-feedback-analyzer"

# ✅ Carrega o pipeline de classificação de sentimento
sentiment_pipeline = pipeline("text-classification", model=modeloHF)

# ✅ Instância do roteador FastAPI
router = APIRouter()

# 📥 Modelo de entrada esperado pela API
class TextoEntrada(BaseModel):
    texto: str

# 🔠 Tradução de rótulos para português
def traduzir_label(label: str) -> str:
    return {
        "Positive": "Positivo",
        "Neutral": "Neutro",
        "Negative": "Negativo"
    }.get(label, label)

# 🧠 Função para analisar o sentimento de um único texto
def analisar_sentimento(texto: str):
    resultado = sentiment_pipeline([texto[:512]])[0]  # Limite de tokens
    sentimento = traduzir_label(resultado["label"])
    confianca = round(resultado["score"], 4)
    return sentimento, confianca

# 🧪 Função para análise em lote
def analisar_sentimentos_lote(textos: list[str], batch_size: int = 16):
    entradas = [t[:512] for t in textos]
    resultados_raw = sentiment_pipeline(entradas, batch_size=batch_size, truncation=True)
    
    resultados_processados = []
    for res in resultados_raw:
        sentimento = traduzir_label(res["label"])
        confianca = round(res["score"], 4)
        resultados_processados.append((sentimento, confianca))
    
    return resultados_processados

# 🚀 Endpoint da API para análise de sentimento
@router.post("/analise")
def analise_sentimento(entrada: TextoEntrada):
    sentimento, confianca = analisar_sentimento(entrada.texto)
    return {
        "sentimento": sentimento,
        "confianca": confianca
    }
