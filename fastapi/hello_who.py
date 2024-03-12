from fastapi import FastAPI, Body

app: FastAPI = FastAPI()

@app.post("/hi")
def greet(body: str = Body(embed=True)):
    return f"hello {body}"