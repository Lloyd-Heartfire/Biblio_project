from sqlalchemy.orm import Session
from models.user import User
from .base import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, User)
    
    def get_all(self):
        return self.db.query(self.model).all()

    def get_by_username(self, username: str):
        return self.db.query(self.model).filter_by(username=username).first()
    
    def get_by_email(self, email: str):
        return self.db.query(self.model).filter_by(email=email).first()
    
    def get_books(self, id_user: int):
        user = self.get(id_user)
        return user.books if user else []