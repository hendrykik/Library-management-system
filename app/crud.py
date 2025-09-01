from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from . import models, schemas
from datetime import datetime

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(models.Book).all()

def get_book(db: Session, serial_number: int):
    return db.query(models.Book).filter(models.Book.serial_number == serial_number).first()

def delete_book(db: Session, serial_number: int):
    db_book = get_book(db, serial_number)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book

def borrow_book(db: Session, serial_number: int, borrower: schemas.BookBorrow):
    db_book = get_book(db, serial_number)
    if db_book and not db_book.is_borrowed:
        db_book.is_borrowed = True
        db_book.borrowed_date = datetime.now()
        db_book.borrower_card_number = borrower.borrower_card_number
        db.commit()
        db.refresh(db_book)
    return db_book

def return_book(db: Session, serial_number: int):
    db_book = get_book(db, serial_number)
    if db_book and db_book.is_borrowed:
        db_book.is_borrowed = False
        db_book.borrowed_date = None
        db_book.borrower_card_number = None
        db.commit()
        db.refresh(db_book)
    return db_book