from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    base_url="https://router.requesty.ai/v1",  # Requesty compatível com OpenAI
    api_key=os.getenv("REQUESTY_API_KEY")
)

class Mensagem(BaseModel):
    pergunta: str
    historico: list  # lista de mensagens anteriores

@app.post("/chat")
async def conversar(mensagem: Mensagem):
    try:
        mensagens = [
            {"role": "system", "content": "Você é um assistente especializado em Python. Responda de forma clara, objetiva e com exemplos didáticos."}
        ]
        mensagens.extend(mensagem.historico)
        mensagens.append({"role": "user", "content": mensagem.pergunta})

        resposta = client.chat.completions.create(
            model="openai/gpt-5-mini",
            messages=mensagens
        )

        conteudo = resposta.choices[0].message.content
        return JSONResponse(content={"resposta": conteudo})

    except Exception as e:
        print(f"[ERRO] {e}")
        raise HTTPException(status_code=500, detail="Erro ao gerar resposta da IA")

@app.get("/")
async def root():
    return FileResponse("index.html")
