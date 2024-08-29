from sqlalchemy.orm import Session
from uuid import UUID, uuid4  
from . import models, schemas

def create_letter(db: Session, letter: schemas.LetterCreate):
    db_letter = models.Letter(
        id=uuid4(),  
        title=letter.title,
        content=letter.content,
        color=letter.color,
        likes=0  
    )
    db.add(db_letter)
    db.commit()
    db.refresh(db_letter)
    return db_letter

def get_letters(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Letter).offset(skip).limit(limit).all()

def get_letter(db: Session, letter_id: UUID):  
    return db.query(models.Letter).filter(models.Letter.id == letter_id).first()

def like_letter(db: Session, letter_id: UUID):  
    db_letter = db.query(models.Letter).filter(models.Letter.id == letter_id).first()
    if db_letter:
        db_letter.likes += 1
        db.commit()
        db.refresh(db_letter)
    return db_letter

def unlike_letter(db: Session, letter_id: UUID):  
    db_letter = db.query(models.Letter).filter(models.Letter.id == letter_id).first()
    if db_letter and db_letter.likes > 0:
        db_letter.likes -= 1
        db.commit()
        db.refresh(db_letter)
    return db_letter

def create_comment(db: Session, comment: schemas.CommentCreate, letter_id: str) -> models.Comment:
    db_comment = models.Comment(**comment.dict(), letter_id=letter_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment