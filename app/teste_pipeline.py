from transformers import pipeline

# 🔄 Carrega o pipeline do Hugging Face
sentiment_pipeline = pipeline("sentiment-analysis", model="ViniciusKhan/senticore-bert-sentiment")

# 🧪 Texto de teste
texto = "Conversei com Alexandre 20/06/22 e me apresentei gostou do contato. Reclamou que solicitou relatórios de logs e que foram enviados com as informações misturadas, resolvido o chamado. Dia 30/06 fiz novo contato e me informou que estava tudo tranquilo com os serviços. O Alexandre e o Felipe tem me acionado sempre que precisam de ajuda com algum chamado ou outra informação referente aos serviços."
resultado = sentiment_pipeline([texto])

# 📋 Resultado
print(resultado)
