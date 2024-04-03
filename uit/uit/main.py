from fastapi import FastAPI, Depends
from sqlmodel import create_engine, SQLModel, Session, select, Field

class Hero(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int = None

sqlite_url = "postgresql://kamilzafar54:0ubRWJhPZt3X@ep-silent-dust-a5r01rvj.us-east-2.aws.neon.tech/testdb?sslmode=require"
engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)

def db_session():
    with Session(engine) as session:
        yield session

app = FastAPI()

@app.get("/")
def read_root(session: Depends[SQLModel, db_session]):
    heroes = session.exec(select(Hero)).all()
    return heroes