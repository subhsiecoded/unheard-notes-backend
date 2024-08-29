from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID  # This is correct for PostgreSQL
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
import uuid

class Letter(Base):
    __tablename__ = "letters"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True) 
    title = Column(String, index=True)
    content = Column(String)
    color = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    likes = Column(Integer, default=0)

    comments = relationship("Comment", back_populates="letter", cascade="all, delete-orphan")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)  
    content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    letter_id = Column(UUID(as_uuid=True), ForeignKey('letters.id')) 

    letter = relationship("Letter", back_populates="comments")
