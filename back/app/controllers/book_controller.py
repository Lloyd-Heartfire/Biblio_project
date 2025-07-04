from repositories.book_repository import BookRepository
from sqlalchemy.orm import Session

class BookController:
    def __init__(self, db: Session):

        # Initialise le controller avec une session et un repository de livres
        self.repo = BookRepository(db)

    def create_book(self, data: dict):

        # Crée un nouveau livre à partir des données fournies
        return self.repo.create(data)

    def delete_book(self, book_id: int):

        # Supprime un livre par son ID s’il existe
        book = self.repo.get(book_id)
        if book:
            self.repo.delete(book_id)
        return book

    def search_by_title(self, title: str):

        # Recherche un livre par son titre
        return self.repo.get_by_title(title)

    def search_by_isbn(self, isbn: str):

        # Recherche un livre par son ISBN
        return self.repo.get_by_isbn(isbn)

    def search_by_favorites(self):

        # Retourne tous les livres marqués comme favoris
        return self.repo.get_favorites()

    def search_by_serie(self, id_serie: int):

        # Retourne les livres associés à une série donnée
        return self.repo.get_by_serie(id_serie)

    def search_by_author(self, author_name: str):

        # Recherche les livres liés à un auteur par nom
        return self.repo.get_by_author(author_name)