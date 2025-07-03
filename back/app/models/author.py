from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .association_tables import author_books

class Author(Base):
    id = Column ("id_author", Integer, primary_key= True, index=True)
    name = Column(String(255), nullable=False, index=True)

    books = relationship("Book", secondary=author_books, back_populates="authors")