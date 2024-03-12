from pydantic import BaseModel

class TodoCreate(BaseModel):
    text: str

class TodoUpdate(TodoCreate):
    id: int