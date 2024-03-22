from fastapi import FastAPI, UploadFile, Depends, File
from sqlmodel import create_engine, select, SQLModel, Session, Field, VARBINARY
from typing import List, Annotated, Optional
from ecom import settings
from contextlib import asynccontextmanager
from pydantic import validator

# Define the SQLModel
class Product(SQLModel, table=True):
    sku: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    description: str = Field(nullable=False)
    price: float = Field(nullable=False)
    slug: str = Field(nullable=False)
    quantity: int = Field(nullable=False)


class Image(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    # product_id: int = Field(foreign_key="product.sku")
    name: Optional[str]
    data: bytes

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

app = FastAPI(title="E-commerce API", version="0.1.0", lifespan=lifespan)

def db_session():
    with Session(engine) as session:
        yield session

@app.post("/image")
async def create_image(image: UploadFile, session: Annotated[Session, Depends(db_session)]):
    image = await image.read()
    image_data = Image(data=image)
    session.add(image_data)
    session.commit()
    session.refresh(image_data)
    return image

@app.post("/product")
def create_product(product: Product, session: Annotated[Session, Depends(db_session)]):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product