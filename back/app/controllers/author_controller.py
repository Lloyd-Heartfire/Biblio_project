from repositories.author_repository import AuthorRepository
from sqlalchemy.orm import Session

class AuthorController:
    def __init__(self, db: Session):
        self.repo = AuthorRepository(db)

    def create_author(self, data: dict):
        return self.repo.create(data)

    def delete_author(self, author_id: int):
        author = self.repo.get(author_id)
        if author:
            self.repo.delete(author_id)
        return author

    def search_by_name(self, name: str):
        return self.repo.get_by_name(name)