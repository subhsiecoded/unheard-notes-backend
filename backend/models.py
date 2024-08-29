from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import pytz
from .database import Base

# Define the IST timezone
IST = pytz.timezone('Asia/Kolkata')

class Letter(Base):
    __tablename__ = "letters"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    color = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(IST))  
    likes = Column(Integer, default=0)

    comments = relationship("Comment", back_populates="letter")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(IST))  
    letter_id = Column(Integer, ForeignKey('letters.id'))

    letter = relationship("Letter", back_populates="comments")
