from model import Creature
from fastapi import FastAPI, Depends

app: FastAPI = FastAPI()

@app.get("/creature")
def get_all() -> list[Creature]:
    from data import get_creature
    return get_creature()

@app.get("/user")
def greet(user_agent: dict = Depends(get_all)) -> dict:
    return {"User-Agent": user_agent}