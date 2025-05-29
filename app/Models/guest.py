from .base import Base
from sqlalchemy import Column,String,Integer


class Guest(Base):
    __tablename__ = "guests"


    id = Column(Integer, primary_key=True)
    name = Column(String)