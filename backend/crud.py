from sqlalchemy.orm import Session
from . import models, schemas

def create_letter(db: Session, letter: schemas.LetterCreate):
    db_letter = models.Letter(
        title=letter.title, 
        content=letter.content, 
        color=letter.color 
    )
    db.add(db_letter)
    db.commit()
    db.refresh(db_letter)
    return db_letter

def get_letters(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Letter).offset(skip).limit(limit).all()

def get_letter(db: Session, letter_id: str):
    return db.query(models.Letter).filter(models.Letter.id == letter_id).first()
