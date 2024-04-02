from contextlib import asynccontextmanager
from sqlmodel import SQLModel, create_engine, Session, select
from fastapi import FastAPI
from . import settings
from .models import User

# Create the database engine
connctionstring = str(settings.DATABASE_URL)

engine = create_engine(connctionstring, pool_recycle=300, connect_args={"sslmode": "require"}) 

# Create the tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating database connection")
    create_db_and_tables()
    yield

def db_session():
    with Session(engine) as session:
        yield session

# with Session(engine) as session:
#     user = session.exec(select(User).filter(User.id == "f2a6242d-7764-4608-a382-f7abda7ae33f")).first()
#     print(user)