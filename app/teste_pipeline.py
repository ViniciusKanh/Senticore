from transformers import pipeline

# 🔄 Carrega o pipeline do Hugging Face
sentiment_pipeline = pipeline("sentiment-analysis", model="ViniciusKhan/senticore-bert-sentiment")

# 🧪 Texto de teste
texto = "O atendimento foi excelente, parabéns!"
resultado = sentiment_pipeline([texto])

# 📋 Resultado
print(resultado)
