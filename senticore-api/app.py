import gradio as gr
from transformers import pipeline

# Carrega modelo do Hugging Face Hub
modeloHF = "ViniciusKhan/bert-nps-feedback-analyzer"
sentiment_pipeline = pipeline("text-classification", model=modeloHF)

def analisar_sentimento(texto):
    resultado = sentiment_pipeline([texto[:512]])[0]
    sentimento = resultado["label"]
    confianca = round(resultado["score"], 4)
    return f"Sentimento: {sentimento}\nConfiança: {confianca}"

demo = gr.Interface(
    fn=analisar_sentimento,
    inputs=gr.Textbox(lines=6, placeholder="Cole aqui o feedback do cliente..."),
    outputs="text",
    title="Senticore – Análise de Sentimentos NPS",
    description="Classificador inteligente baseado em BERT para identificar sentimentos em textos de feedback e NPS."
)

demo.launch()
