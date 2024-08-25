from pydantic import BaseModel
from datetime import datetime

class LetterBase(BaseModel):
    title: str
    content: str
    color: str

class LetterCreate(LetterBase):
    pass

class Letter(LetterBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
