from sqlmodel import SQLModel, Field, Relationship, ColumnDefault, Column, Enum, ARRAY
import enum
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime

# Define the SQLModel
class Product(SQLModel, table=True):
    sku: UUID = Field(default=ColumnDefault(uuid4), primary_key=True)
    name: str = Field(nullable=False)
    description: str = Field(nullable=False)
    price: float = Field(nullable=False)
    slug: str = Field(nullable=False)
    image_1: str 
    image_2: str 

class TokenData(SQLModel):
    username: str

class Token(SQLModel):
    access_token: str
    token_type: str

class User(SQLModel, table=True):
    id: Optional[UUID] = Field(primary_key=True, default=ColumnDefault(uuid4), index=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True, nullable=False)
    hashed_password: str = Field(index=True, nullable=False)

class Cart(Product, table=True):
    id: Optional[int] = Field(primary_key=True)
    product_total: float
    product_size: str
    quantity: int = Field(nullable=False)

def get_current_time(execution_context):
    return datetime.now()

class Order(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    user_id: int
    ordered_at: datetime = Field(ColumnDefault(get_current_time))
    product_id: int
    quantity: int
    total: float