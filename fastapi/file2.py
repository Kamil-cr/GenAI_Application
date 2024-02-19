from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get("/hi")
def greet():
    return "Hello? World"

if "__name__" == "__main__":
    import uvicorn
    uvicorn.run("file2: app", reload=True)