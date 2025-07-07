from sqlalchemy.orm import Session
from app.models.author import Author
from .base import BaseRepository

class AuthorRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, Author)

    def get_all(self):
        return self.db.query(self.model).all()

    def get_by_name(self, name: str):
        return self.db.query(self.model).filter_by(name=name).first()