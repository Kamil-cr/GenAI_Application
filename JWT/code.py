from typing import  Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app: FastAPI = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
def root():
    print(OAuth2PasswordBearer.__doc__)
    return {"message": "Hello World"}

@app.get("/token")
def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}