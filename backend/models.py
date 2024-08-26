from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Letter(Base):
    __tablename__ = "letters"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    color = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    likes = Column(Integer, default=0)  # Add this line

    comments = relationship("Comment", back_populates="letter")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    letter_id = Column(Integer, ForeignKey('letters.id'))
    
    letter = relationship("Letter", back_populates="comments")
