# 🤖 Senticore – Análise de Sentimentos com BERT (via Hugging Face Hub)

O **Senticore** é uma API reutilizável para análise de sentimentos baseada em textos livres, como resumos de interações com clientes. Utiliza o modelo `bert-nps-feedback-analyzer`, treinado para compreender nuances de sentimentos em português, especialmente em frases longas e técnicas como feedbacks NPS.

---

## 🚀 Funcionalidades

- 🔍 Análise de sentimentos com 3 classes: `Positivo`, `Neutro`, `Negativo`
- 🌐 Robusto para textos longos e multilíngues (XLM-RoBERTa)
- 📈 Retorna grau de confiança (score entre 0 e 1)
- 🔁 API REST reutilizável com FastAPI
- ☁️ Modelo carregado diretamente do Hugging Face (sem download manual)

---

## 🧠 Modelo Utilizado

- **Nome:** [`ViniciusKhan/bert-nps-feedback-analyzer`](https://huggingface.co/ViniciusKhan/bert-nps-feedback-analyzer)
- **Base:** `cardiffnlp/twitter-xlm-roberta-base-sentiment`
- **Tarefa:** `text-classification`
- **Classes:** `Negative`, `Neutral`, `Positive`

---

## 📁 Estrutura do Projeto

```
Senticore/
├── app/
│   ├── main.py                   # Inicializa API com FastAPI
│   └── routes/
│       └── sentiment.py          # Endpoint de análise de sentimento
├── 0-Datasets/
│   └── Relacionamento.xlsx       # Dados originais
├── Analise_Sentimento_Local.py   # (obsoleto) - substituído por API com modelo online
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ✅ Como Executar a API

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute a API localmente:

```bash
uvicorn app.main:app --reload
```

3. Acesse a documentação interativa:

```
http://127.0.0.1:8000/docs
```

---

## 📦 Como funciona a inferência

O modelo retorna diretamente um rótulo (`label`) e um score de confiança. Exemplo de resposta da API:

```json
{
  "sentimento": "Positivo",
  "confianca": 0.8453
}
```

---

## 📊 Exemplo de Saída

| Resumo                                                                 | Sentimento | Confianca |
|------------------------------------------------------------------------|------------|-----------|
| Cliente elogiou o serviço, mas mencionou instabilidade no sistema.     | Neutro     | 0.6032    |
| Nada funciona, péssimo atendimento.                                    | Negativo   | 0.9021    |
| Muito satisfeito com a entrega.                                        | Positivo   | 0.8714    |

---

## 🧪 Testado em

- Python 3.11
- Windows 10 (PowerShell + VSCode)
- FastAPI 0.110+
- Transformers v4.41+
- Torch 2.2+

---

## 👨‍💻 Autor

Desenvolvido por **Vinicius de Souza Santos**  
🎓 Eng. da Computação | Especialista em ML, Data Analysis e Software

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
