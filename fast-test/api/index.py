from fastapi import FastAPI
from api.functions import get_response
app: FastAPI = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/product")
def product(prompt: str):
    result = get_response(prompt)
    return {"response": result}