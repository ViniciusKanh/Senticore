from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from app.routes.sentiment import router as sentiment_router
import pandas as pd
import uuid
import os

app = FastAPI(
    title="Senticore API com Upload",
    description="API de análise de sentimentos via upload de Excel",
    version="1.0.0"
)

app.include_router(sentiment_router)
templates = Jinja2Templates(directory="app/templates")

UPLOAD_DIR = "app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Página HTML principal
@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Endpoint para processar upload do Excel
@app.post("/upload_excel/", response_class=HTMLResponse)
async def upload_excel(request: Request, file: UploadFile = File(...)):
    # Salvar arquivo temporariamente
    file_id = uuid.uuid4().hex
    temp_path = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    # Ler dados
    df = pd.read_excel(temp_path)
    if "Resumo" not in df.columns:
        return {"erro": "Coluna 'Resumo' não encontrada no arquivo."}

    # Processar sentimentos
    from app.routes.sentiment import analisar_sentimento
    resultados = df["Resumo"].fillna("").apply(analisar_sentimento)
    df["Sentimento"], df["Confianca"] = zip(*resultados)

    # Salvar novo arquivo para download posterior
    output_filename = f"{file_id}_resultado.xlsx"
    output_path = os.path.join(UPLOAD_DIR, output_filename)
    df.to_excel(output_path, index=False)

    # Gerar HTML da tabela para exibir na página
    table_html = df.to_html(classes="result-table", index=False)

    # Exibir página com resultado e link para download
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "table_html": table_html,
            "download_url": f"/download/{output_filename}"
        },
    )


# Rota para download do arquivo processado
@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    return FileResponse(
        path=file_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="resultado_sentimento.xlsx",
    )
