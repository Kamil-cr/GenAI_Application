from contextlib import asynccontextmanager
from typing import Optional, Annotated
# from uitclass import settings
from sqlmodel import Field, Session, SQLModel, create_engine, Column, String, Integer
from fastapi import FastAPI, Depends
import curd
from dotenv import load_dotenv, get_key

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
async def lifespan(app: FastAPI):
    print("Creating tables..")
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan, title="Hello World API with DB", 
    version="0.0.1")

def db_session():
    with Session(engine) as session:
        yield session


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/todos", response_model=Todo)
def create_todo(todo: str, session: Annotated[Session, Depends(db_session)]):
        todo = curd.create_todo(todo, session)
        # session.add(todo)
        # session.commit()
        # session.refresh(todo)
        return todo


@app.get("/todos", response_model=list[Todo])
def read_todos(session: Annotated[Session, Depends(db_session)]):
        # todos = session.exec(select(Todo)).all()
        todos = curd.read_todos(session)
        return todos

@app.get("/todos/{todo_id}", response_model=Todo)
def read_todo(todo_id: int, session: Annotated[Session, Depends(db_session)]):
        # todo = session.get(Todo, todo_id)
        todo = curd.read_todo(todo_id, session)
        return todo

@app.put("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int, session: Annotated[Session, Depends(db_session)]):
        todo = curd.delete_todo(todo_id, session)
        # todo = session.get(Todo, todo_id)
        # session.delete(todo)
        # session.commit()
        return todo