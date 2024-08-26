from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class LetterBase(BaseModel):
    title: str
    content: str
    color: str

class LetterCreate(LetterBase):
    pass

class Letter(LetterBase):
    id: int
    created_at: datetime
    likes: int
    comments: List[Comment] = []

    class Config:
        orm_mode = True
