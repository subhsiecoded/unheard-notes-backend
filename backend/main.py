from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud, database
from .database import engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","https://unheardnotes.vercel.app"],

    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
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
def read_letter(letter_id: int, db: Session = Depends(get_db)):  # Changed letter_id type to int
    db_letter = crud.get_letter(db, letter_id=letter_id)
    if db_letter is None:
        raise HTTPException(status_code=404, detail="Letter not found")
    return db_letter
