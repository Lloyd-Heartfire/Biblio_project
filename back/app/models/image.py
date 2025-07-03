from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from .base import Base
from .association_tables import book_images

class Image(Base):
    id = Column ("id_image", Integer, primary_key= True, index=True)
    url = Column(Text, nullable=False)
    name = Column(String(255), nullable=True, index=True)

    books = relationship("Book", secondary=book_images, back_populates="images")