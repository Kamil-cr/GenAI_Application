from sqlmodel import SQLModel, Field, Relationship, ColumnDefault, Column, Enum, ARRAY
import enum
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime, timedelta

class ProductBase(SQLModel):
    name: str = Field(nullable=False)
    description: str = Field(nullable=False)
    price: float = Field(nullable=False)
    slug: str = Field(nullable=False)
    image1: str = Field(nullable=False)
    image2: str = Field(nullable=False)

# Define the SQLModel
class Product(ProductBase, table=True):
    sku: UUID = Field(index=True, primary_key=True)

class ProductCreate(ProductBase):
    pass

class TokenData(SQLModel):
    username: str

class Token(SQLModel):
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int

class UserBase(SQLModel):
    username: str = Field(nullable=False)
    hashed_password: str = Field(nullable=False)

class Userlogin(UserBase):
    pass

class User(UserBase, table=True):
    id: Optional[UUID] = Field(primary_key=True, index=True)
    email: str = Field(index=True, unique=True, nullable=False)

class UserCreate(UserBase):
    email: str

# class Cart(Product, table=True):
#     id: Optional[int] = Field(primary_key=True)
#     product_total: float
#     product_size: str
#     quantity: int = Field(nullable=False)

class Order(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    user_id: int
    ordered_at: datetime
    product_id: int
    quantity: int
    total: float


class Token(SQLModel):
    access_token: str
    token_type: str
    expires_in: int | timedelta
    refresh_token: str

class TokenData(SQLModel):
    username: str | None = None
    id: UUID | None = None
