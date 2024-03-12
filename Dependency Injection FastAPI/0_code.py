from fastapi import FastAPI, Depends, Query
from typing import Annotated

app: FastAPI = FastAPI()

def login_user(username: str = Query(None), password: str = Query(None)):
    if username == "admin" and password == "admin":
        return {"mesage": "Login Success"}
    else:
        return {"message": "Login Failed"}

@app.get("/login")
async def login(user: Annotated[dict, Depends(login_user)]):
    return user