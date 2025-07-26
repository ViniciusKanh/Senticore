
# 🤖 Senticore – Análise de Sentimentos com BERT Local

O **Senticore** é uma API reutilizável para análise de sentimentos baseada em textos livres, como resumos de interações com clientes. Utiliza o modelo BERT Multilingual treinado para análise de sentimentos com 5 classes, operando de forma **100% local** e compatível com ambientes offline.

---

## 🚀 Funcionalidades

- 🔍 Análise de sentimentos usando modelo local (BERT)
- 🌐 Compatível com múltiplos idiomas
- 📈 Geração de confiança (probabilidade) da classificação
- 🔁 API reutilizável para integração com sistemas e dashboards
- 📥 Baixa e salva o modelo automaticamente
- ✅ Pode ser usado com ou sem conexão com a internet

---

## 🧠 Modelo Utilizado

- **Nome:** `nlptown/bert-base-multilingual-uncased-sentiment`
- **Fonte:** [Hugging Face 🤗](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)
- **Saída:** Sentimentos entre 1 e 5 estrelas

| Estrelas | Sentimento |
|----------|------------|
| 1-2      | Negativo   |
| 3        | Neutro     |
| 4-5      | Positivo   |

---

## 📁 Estrutura do Projeto

```
Senticore/
├── app/
│   ├── download_model.py        # Baixa e salva o modelo localmente
│   └── model/                   # (Ignorado no GitHub) Contém o modelo BERT
├── 0-Datasets/
│   └── Relacionamento.xlsx      # Dados originais
├── Analise_Sentimento_Local.py # Executa análise local e salva resultados
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📥 Download do Modelo

Para manter o repositório leve, o modelo **não é incluído no GitHub**.

### 🛠️ Baixe executando:

```bash
python app/download_model.py
```

Isso criará a pasta `./app/model/bert-multilingual-sentiment/` com todos os arquivos necessários para execução local.

---

## ✅ Como Executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Baixe o modelo:

```bash
python app/download_model.py
```

3. Execute a análise local:

```bash
python Analise_Sentimento_Local.py
```

4. Verifique o resultado:

> O arquivo `Relacionamento_Analisado_Local.xlsx` será gerado com as colunas `Sentimento` e `Confianca`.

---

## 📊 Exemplo de Saída

| Resumo                                            | Sentimento | Confianca |
|--------------------------------------------------|------------|-----------|
| Cliente elogiou o serviço, mas mencionou instabilidade no sistema. | Neutro     | 0.6032    |
| Nada funciona, péssimo atendimento.              | Negativo   | 0.9021    |
| Muito satisfeito com a entrega.                  | Positivo   | 0.8714    |

---

## 🧪 Testado em

- Python 3.11
- Windows 10 (PowerShell + VSCode)
- HuggingFace Transformers v4.41+
- Torch 2.2+

---

## 👨‍💻 Autor

Desenvolvido por **Vinicius de Souza Santos**  
🎓 Eng. da Computação | Especialista em ML, Data Analysis e Software

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
