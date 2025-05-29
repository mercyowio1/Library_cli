from .base import Base
from sqlalchemy import Column, Integer, ForeignKey,DateTime
from datetime import datetime, timezone


class BorrowedBook(Base):
    __tablename__ = "borrowed_books"

    id = Column(Integer, primary_key=True)
    members_id = Column(Integer, ForeignKey("members.id"))
    books_id = Column(Integer, ForeignKey("books.id"))
    borrowed_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    return_date = Column(DateTime, nullable=True)