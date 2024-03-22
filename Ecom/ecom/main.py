from fastapi import FastAPI, Depends, Up
from sqlmodel import create_engine, select, SQLModel,Relationship, Session, Field
from datetime import datetime
from typing import List, Annotated
from ecom import settings
from contextlib import asynccontextmanager

# Define the SQLModel
class Product(SQLModel, table=True):
    sku: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    description: str = Field(nullable=False)
    price: float = Field(nullable=False)
    slug: str = Field(nullable=False)
    quantity: int = Field(nullable=False)
    images: List["ProductImage"] = Relationship(back_populates="product")

class ProductImage(SQLModel, table=True):
    id: int = Field(primary_key=True)
    product_id: int = Field(foreign_key="product.sku")
    name: str
    filetype: str
    product: Product = Relationship(back_populates="images", link_model=Product)

# Create the database engine
connection_string = str(settings.TEST_DATABASE_URL)

engine = create_engine(connection_string, pool_recycle=300, connect_args={"sslmode": "require"})

# Create the tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating database connection")
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan, title="E-commerce API", version="0.1.0")

def db_session():
    with Session(engine) as session:    
        yield session

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/products", response_model=List[Product])
def read_products(session: Annotated[Session, Depends(db_session)]):
    products = session.exec(select(Product)).all()
    return products

@app.get("/image")
def read_image(session: Annotated[Session, Depends(db_session)]):
    images = session.exec(select(ProductImage)).all()
    return images