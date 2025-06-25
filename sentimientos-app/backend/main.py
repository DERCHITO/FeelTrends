# FastAPI core
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Sentimientos API - MVP"}
