# app/main.py

from fastapi import FastAPI
from app.routes import sentiment

app = FastAPI(
    title="Senticore – API de Análise de Sentimentos",
    description="Classifica sentimentos de textos NPS usando BERT especializado",
    version="2.0"
)

# ✅ Registro de rotas
app.include_router(sentiment.router, prefix="/api")
