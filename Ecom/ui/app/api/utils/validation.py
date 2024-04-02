from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import timedelta
from typing import Optional
from .models import Product

class UserCreate(BaseModel):
    id: Optional[UUID]
    username: str
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int | timedelta
    refresh_token: str

class TokenData(BaseModel):
    username: str | None = None
    id: UUID | None = None

class UserLogin(BaseModel):
    email:EmailStr
    hashed_password:str

class Cartcreate(BaseModel):
    id: Optional[int]
    product: Product