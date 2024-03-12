from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlmodel import Session, create_engine, SQLModel, Field, Column, String
from typing import Annotated, Optional
from utils import curd
from dotenv import get_key

class Todo(SQLModel, table=True):
    __tablename__: str = "Too"
    id: Optional[int] = Field(primary_key=True, index=True)
    todo: str = Column(String, index=True)

DATABASE_URL = get_key(".env", "DATABASE_URL")

connection_string = str(DATABASE_URL)

engine = create_engine(
    connection_string, connect_args={"sslmode": "require"}, pool_recycle=300
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan():
    print("Creating tables..")
    create_db_and_tables()
    yield

app = FastAPI()

def db_session():
    with Session(engine) as session:    
        yield session

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/todos", response_model=list[Todo])
def read_todos(session: Annotated[Session, Depends(db_session)]):
        todos = curd.read_todos(session)
        return todos

@app.post("/todos", response_model=Todo)
def create_todos(todo: str, session: Annotated[Session, Depends(db_session)]):
    return curd.create_todos(todo, session)

@app.delete("/todos", response_model=dict)
def delete_todos(id: int, session: Annotated[Session, Depends(db_session)]):
    return curd.delete_todos(id, session)

@app.patch("/todos", response_model=Todo)
def update_todos(id: int, update_todo: str, session: Annotated[Session, Depends(db_session)]):
    return curd.update_todos(id, update_todo, session)