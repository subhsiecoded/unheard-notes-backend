from fastapi import FastAPI, HTTPException, Depends, Path
from sqlalchemy.orm import Session
from . import models, schemas, crud, database
from .database import engine
from fastapi.middleware.cors import CORSMiddleware
from uuid import UUID

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://unheardnotes.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new letter
@app.post("/api/letters", response_model=schemas.Letter)
def create_letter(letter: schemas.LetterCreate, db: Session = Depends(get_db)):
    return crud.create_letter(db=db, letter=letter)

# Read letters with pagination
@app.get("/api/letters", response_model=list[schemas.Letter])
def read_letters(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    letters = crud.get_letters(db, skip=skip, limit=limit)
    return letters

# Read a specific letter by ID
@app.get("/api/letters/{letter_id}", response_model=schemas.Letter)
def read_letter(letter_id: UUID, db: Session = Depends(get_db)):
    db_letter = crud.get_letter(db, letter_id=letter_id)
    if db_letter is None:
        raise HTTPException(status_code=404, detail="Letter not found")
    return db_letter

# Like a specific letter by ID
@app.post("/api/letters/{letter_id}/like", response_model=schemas.Letter)
def like_letter(letter_id: UUID, db: Session = Depends(get_db)):
    db_letter = crud.like_letter(db, letter_id=letter_id)
    if db_letter is None:
        raise HTTPException(status_code=404, detail="Letter not found")
    return db_letter

@app.post("/api/letters/{letter_id}/unlike", response_model=schemas.Letter)
def unlike_letter(letter_id: UUID, db: Session = Depends(get_db)):
    letter = crud.unlike_letter(db, letter_id)
    if not letter:
        raise HTTPException(status_code=404, detail="Letter not found")
    return letter

# Add a comment to a specific letter by ID
@app.post("/api/letters/{letter_id}/comments", response_model=schemas.Comment)
def add_comment(letter_id: UUID, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment, letter_id=letter_id)
