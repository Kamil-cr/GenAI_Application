from contextlib import asynccontextmanager
from typing import Annotated, Optional
from fastapi import FastAPI, Depends
from sqlalchemy import Field, Session, SQLModel, create_engine, select, table

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: Optional[str] = Field(index=True)

