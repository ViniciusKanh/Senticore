# ✅ Imagem base oficial do Python
FROM python:3.11-slim

# ✅ Variáveis de ambiente
ENV HF_HOME=/root/.cache/huggingface \
    TRANSFORMERS_CACHE=/root/.cache/huggingface/transformers \
    HF_TOKEN="your_token_if_needed"

# ✅ Diretório de trabalho
WORKDIR /app

# ✅ Copia arquivos para o container
COPY requirements.txt .
COPY app/ ./app/

# ✅ Instala as dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# ✅ Exposição da porta padrão do FastAPI
EXPOSE 7860

# ✅ Comando de inicialização com uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
