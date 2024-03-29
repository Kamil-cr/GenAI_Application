from fastapi import FastAPI

app = FastAPI() 
@app.get("/") 
def index(): 
    return {"Hello": "World"} 

@app.get("/items/{item_id}") 
def read_item(item_id: int, q: str) -> dict[str, int|str]: 
    return {"item_id": item_id, "q": q}