from repositories.user_repository import UserRepository
from sqlalchemy.orm import Session

class UserController:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create_user(self, data: dict):
        return self.repo.create(data)

    def delete_user(self, user_id: int):
        user = self.repo.get(user_id)
        if user:
            self.repo.delete(user_id)
        return user

    def search_by_username(self, username: str):
        return self.repo.get_by_username(username)

    def list_books(self, user_id: int):
        return self.repo.get_books(user_id)