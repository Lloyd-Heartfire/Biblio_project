from sqlalchemy import Column, Integer, String, Text

from .base import Base

class Serie(Base):
    __tablename__ = "series"
    
    id = Column ("id_serie", Integer, primary_key= True, index=True)
    name = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)