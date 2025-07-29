---
license: mit
title: Senticore – Análise de Sentimentos
sdk: gradio
emoji: 🚀
colorFrom: green
colorTo: green
pinned: false
---

# 🚀 Senticore – Análise de Sentimentos com FastAPI + BERT

O **Senticore API** é uma solução de inferência de sentimentos baseada em BERT e implementada com FastAPI, hospedada como um Space no Hugging Face. Ele recebe um texto livre e retorna a polaridade (`Positivo`, `Neutro`, `Negativo`) com sua respectiva confiança.

---

## ✅ Funcionalidades

- Classificação de sentimento em português (positivo, neutro ou negativo)
- Uso do modelo `ViniciusKhan/bert-nps-feedback-analyzer`
- API RESTful com FastAPI
- Suporte a múltiplas chamadas (batch)
- Deploy no Hugging Face Spaces via Docker

---

## 🚀 Como usar

Após o deploy no Hugging Face Spaces, acesse a URL da sua API e envie uma requisição `POST` com um JSON como este:

```json
{
  "texto": "Muito satisfeito com o atendimento e suporte da equipe."
}
```

A resposta será:

```json
{
  "sentimento": "Positivo",
  "confianca": 0.9453
}
```

---

## 📂 Estrutura do Projeto

```
senticore-api/
├── app/
│   ├── main.py
│   └── routes/
│       └── sentiment.py
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 👨‍💻 Autor

Desenvolvido por **Vinicius de Souza Santos**  
🎓 Eng. da Computação | Especialista em ML, Data Analysis e Software

---

## 📄 Licença

Licenciado sob os termos da Licença MIT.