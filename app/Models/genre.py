from .base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", secondary="bookgenres", back_populates="genres")