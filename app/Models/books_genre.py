from .base import Base
from sqlalchemy import Column, Integer, ForeignKey

class BookGenre(Base):
    __tablename__ = 'bookgenres'

    books_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    genre_id = Column(Integer, ForeignKey("genres.id"), primary_key=True)