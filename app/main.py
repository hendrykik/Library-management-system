from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library API", description="Simple library management system")

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, serial_number=book.serial_number)
    if db_book:
        raise HTTPException(status_code=400, detail="Book with this serial number already exists")
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=list[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.delete("/books/{serial_number}")
def delete_book(serial_number: str, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db, serial_number=serial_number)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}

@app.put("/books/{serial_number}/borrow", response_model=schemas.Book)
def borrow_book(serial_number: str, borrower: schemas.BookBorrow, db: Session = Depends(get_db)):
    db_book = crud.borrow_book(db, serial_number=serial_number, borrower=borrower)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    if db_book.is_borrowed and db_book.borrower_card_number != borrower.borrower_card_number:
        raise HTTPException(status_code=400, detail="Book is already borrowed")
    return db_book

@app.put("/books/{serial_number}/return", response_model=schemas.Book)
def return_book(serial_number: str, db: Session = Depends(get_db)):
    db_book = crud.return_book(db, serial_number=serial_number)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book