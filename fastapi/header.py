from fastapi import FastAPI, Header

app: FastAPI = FastAPI()

@app.get("/hi")
def greet(user_agent: str = Header()):
    return {"User-Agent": user_agent}