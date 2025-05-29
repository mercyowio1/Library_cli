from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    available_copies = Column(Integer)

    borrowed_books = relationship("BorrowedBook", backref="book")
    guest_readings = relationship("GuestReading", backref="book")
    genres = relationship("Genre", secondary="bookgenres", back_populates="books")