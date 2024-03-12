from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get("/hi")
def greet():
    return "Hello? World"

@app.get("/hi/{name}")
def greet_name(name: str):
    return f"Hello, {name}!"

if "__name__" == "__main__":
    import uvicorn
    uvicorn.run("file2: app", reload=True)