from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    age: int
    country: str
    area: str