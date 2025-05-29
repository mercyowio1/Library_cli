from .base import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime,timezone

class GuestReading(Base):
    __tablename__ = "guest_readings"

    id = Column(Integer, primary_key=True)
    books_field = Column(Integer, ForeignKey("books.id"))
    guest_id = Column(Integer, ForeignKey("guests.id"))
    time = Column(DateTime, default=lambda :datetime.now(timezone.utc))