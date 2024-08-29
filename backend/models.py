from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import pytz
from .database import Base

# Define the IST timezone
IST = pytz.timezone('Asia/Kolkata')

# Function to get the current time in IST
def current_time_in_ist():
    return datetime.now(IST)

class Letter(Base):
    __tablename__ = "letters"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, index=True)
    content = Column(String)
    color = Column(String)
    created_at = Column(DateTime, default=current_time_in_ist)
    likes = Column(Integer, default=0)

    comments = relationship("Comment", back_populates="letter")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    content = Column(String)
    created_at = Column(DateTime, default=current_time_in_ist)
    letter_id = Column(UUID(as_uuid=True), ForeignKey('letters.id'))

    letter = relationship("Letter", back_populates="comments")
