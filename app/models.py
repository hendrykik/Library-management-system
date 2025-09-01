from sqlalchemy import Column, String, Boolean, DateTime, Integer
from sqlalchemy.sql import func
from .database import Base

class Book(Base):
    __tablename__ = "books"

    serial_number = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    is_borrowed = Column(Boolean, default=False)
    borrowed_date = Column(DateTime, nullable=True)
    borrower_card_number = Column(Integer, nullable=True)