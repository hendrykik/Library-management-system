from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional

class BookCreate(BaseModel):
    serial_number: int = Field(..., ge=100000, le=999999)
    title: str
    author: str

class BookBorrow(BaseModel):
    borrower_card_number: int = Field(..., ge=100000, le=999999)

class Book(BaseModel):
    serial_number: int
    title: str
    author: str
    is_borrowed: bool
    borrowed_date: Optional[datetime] = None
    borrower_card_number: Optional[int] = None

    class Config:
        from_attributes = True