import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EchoIn(BaseModel):
    message: str

@app.get("/")
def health():
    return {"status": "läuft 🚀"}

@app.post("/echo")
def echo(data: EchoIn):
    return {"reply": f"Du hast gesagt: {data.message}"}
