from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from .base import Base
from .association_tables import user_books

class User(Base):
    __tablename__ = "users"

    id = Column ("id_user", Integer, primary_key= True, index=True)
    username = Column(String(255), nullable=False, index=True)
    email = Column(String(255), nullable=False)
    password = Column(Text, nullable=False)
    role = Column(String(255), nullable=False)

    books = relationship("Book", secondary=user_books, back_populates="users")