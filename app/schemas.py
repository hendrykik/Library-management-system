from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class BookCreate(BaseModel):
    serial_number: str = Field(..., min_length=6, max_length=6)
    title: str
    author: str

class BookBorrow(BaseModel):
    borrower_card_number: str = Field(..., min_length=6, max_length=6)

class Book(BaseModel):
    serial_number: str
    title: str
    author: str
    is_borrowed: bool
    borrowed_date: Optional[datetime] = None
    borrower_card_number: Optional[str] = None

    class Config:
        from_attributes = True