from .base import Base
from sqlalchemy import Integer,String,Column
from sqlalchemy.orm import relationship


class Member(Base):
    __tablename__="members"

    id= Column(Integer,primary_key=True)
    _name = Column("name",String)
    _email =Column("email",String)
    membership_no =Column(Integer)


    borrowed_books = relationship("BorrowedBook", backref="member")


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value:str):
        if len(value) < 4 or len(value) > 25:
            raise ValueError ("Name should be more than 3 or 25")
        else:
            self._name = value

    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        if "@" not in value or "." not in value:
            raise ValueError("Please enter a valid email address.")
        else:
            self._email = value