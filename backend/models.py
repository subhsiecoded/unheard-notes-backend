from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID  # Import UUID from PostgreSQL dialect
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Letter(Base):
    __tablename__ = "letters"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    color = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)  # You can change to timezone-aware if needed
    likes = Column(Integer, default=0)

    comments = relationship("Comment", back_populates="letter")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)  # Same here
    letter_id = Column(UUID, ForeignKey('letters.id'))  # Change to UUID type
    
    letter = relationship("Letter", back_populates="comments")
