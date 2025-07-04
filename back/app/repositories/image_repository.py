from sqlalchemy.orm import Session
from models.image import Image
from .base import BaseRepository

class ImageRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, Image)
    
    def get_all(self):
        return self.db.query(self.model).all()

    def get_by_url(self, url: str):
        return self.db.query(self.model).filter_by(url=url).first()

    def get_by_name(self, name: str):
        return self.db.query(self.model).filter_by(name=name).first()