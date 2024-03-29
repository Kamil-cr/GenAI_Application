from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlmodel import Session, create_engine, SQLModel, Field
from typing import Annotated, Optional
from utils import crud
from fastapi_todo import settings

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    todo: str = Field(index=True)

connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)

engine = create_engine(
    connection_string, connect_args={"sslmode": "require"}, pool_recycle=300
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables..")
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan, title="FastAPI Todo", version="0.1")

def db_session():
    with Session(engine) as session:    
        yield session

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/todos", response_model=list[Todo])
def read_todos(session: Annotated[Session, Depends(db_session)]):
        todos = crud.read_todos(session)
        return todos

@app.post("/todos", response_model=Todo)
def create_todos(todo: str, session: Annotated[Session, Depends(db_session)]):
    return crud.create_todos(todo, session)

@app.delete("/todos", response_model=dict)
def delete_todos(id: int, session: Annotated[Session, Depends(db_session)]):
    return crud.delete_todos(id, session)

@app.patch("/todos", response_model=Todo)
def update_todos(id: int, update_todo: str, session: Annotated[Session, Depends(db_session)]):
    return crud.update_todos(id, update_todo, session)