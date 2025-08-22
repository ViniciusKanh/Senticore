
import gradio as gr
import pandas as pd
from transformers import pipeline
import uuid

# 🔍 Carrega modelo do Hugging Face
modeloHF = "ViniciusKhan/bert-nps-feedback-analyzer"
sentiment_pipeline = pipeline("text-classification", model=modeloHF)

# 🧠 Função de inferência para texto simples
def analisar_sentimento(texto):
    texto = texto.lower()  # Normaliza para evitar sensibilidade a maiúsculas
    resultado = sentiment_pipeline([texto[:512]])[0]
    sentimento = resultado["label"]
    confianca = round(resultado["score"], 4)
    return f"🔹 Sentimento: {sentimento}\n🔹 Confiança: {confianca}"

# 🧠 Função de inferência para planilhas
def analisar_arquivo(file):
    try:
        df = pd.read_excel(file.name)
    except Exception:
        return "❌ Erro ao ler o arquivo. Certifique-se de que é um .xlsx válido.", None

    if "Resumo" not in df.columns:
        return "❌ A coluna obrigatória 'Resumo' não foi encontrada.", None

    textos = df["Resumo"].fillna("").astype(str).str.lower().str[:512].tolist()
    resultados = sentiment_pipeline(textos, truncation=True)

    df["Sentimento_Class"] = [r["label"] for r in resultados]
    df["Confianca"] = [round(r["score"], 4) for r in resultados]

    nome_saida = f"/tmp/resultado_sentimento_{uuid.uuid4().hex[:8]}.xlsx"
    df.to_excel(nome_saida, index=False)

    return df, nome_saida

# 🎨 Interface Gradio com layout aprimorado
with gr.Blocks(title="Senticore – Análise de Sentimentos NPS") as demo:
    gr.Markdown(
        """
        <h1 style='text-align: center; color: #00A86B;'>🤖 Senticore</h1>
        <p style='text-align: center;'>Classificador BERT inteligente para análise de sentimentos em feedbacks NPS</p>
        """)

    with gr.Tab("📝 Texto Individual"):
        with gr.Row():
            entrada_texto = gr.Textbox(lines=5, label="Texto do cliente", placeholder="Cole aqui o feedback...")
        with gr.Row():
            botao_texto = gr.Button("🔍 Analisar")
        with gr.Row():
            saida_texto = gr.Textbox(label="Resultado da Análise", lines=2)

        botao_texto.click(analisar_sentimento, entrada_texto, saida_texto)

    with gr.Tab("📂 Lote via Excel"):
        gr.Markdown("💡 O arquivo deve conter uma coluna chamada **Resumo** com os textos a serem analisados.")

        entrada_arquivo = gr.File(file_types=[".xlsx"], label="📁 Envie um arquivo Excel")
        botao_excel = gr.Button("📊 Analisar Arquivo")
        saida_tabela = gr.Dataframe(label="📄 Tabela com Sentimentos", interactive=False)
        download_link = gr.File(label="📥 Download do Excel Processado")

        botao_excel.click(
            fn=analisar_arquivo,
            inputs=entrada_arquivo,
            outputs=[saida_tabela, download_link]
        )

demo.launch()
