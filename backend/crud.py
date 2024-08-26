from sqlalchemy.orm import Session
from . import models, schemas

def create_letter(db: Session, letter: schemas.LetterCreate):
    db_letter = models.Letter(title=letter.title, content=letter.content, color=letter.color)
    db.add(db_letter)
    db.commit()
    db.refresh(db_letter)
    return db_letter

def get_letters(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Letter).offset(skip).limit(limit).all()

def get_letter(db: Session, letter_id: int):
    return db.query(models.Letter).filter(models.Letter.id == letter_id).first()

def like_letter(db: Session, letter_id: int):
    db_letter = db.query(models.Letter).filter(models.Letter.id == letter_id).first()
    if db_letter:
        db_letter.likes += 1
        db.commit()
        db.refresh(db_letter)
    return db_letter

def create_comment(db: Session, comment: schemas.CommentCreate, letter_id: int):
    db_comment = models.Comment(content=comment.content, letter_id=letter_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
