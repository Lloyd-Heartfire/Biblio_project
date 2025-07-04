# Importe la classe Book depuis le module models.book
from models.book import Book

# Importe la classe Author depuis le module models.author
from models.author import Author

# Importe la classe de base pour les repositories
from .base import BaseRepository

# Importe la classe Session pour gérer la base de données
from sqlalchemy.orm import Session


class BookRepository(BaseRepository):
    def __init__(self, db: Session):
        # Initialise le repository avec le modèle Book
        super().__init__(db, Book)

    def get_by_title(self, title: str):
        # Retourne le premier livre correspondant au titre donné
        return self.db.query(self.model).filter_by(title=title).first()

    def get_by_isbn(self, isbn: str):

        # Cherche le premier livre avec cet ISBN
        return self.db.query(self.model).filter_by(isbn=isbn).first()

    def get_favorites(self):

        # Cherche tous les livres marqués comme favoris
        return self.db.query(self.model).filter_by(is_favorite=True).all()

    def get_by_serie(self, id_serie: int):

        # Cherche tous les livres de cette série
        return self.db.query(self.model).filter_by(id_serie=id_serie).all()

    def get_by_author(self, author_name: str):

        # Retourne tous les livres dont l'auteur contient le nom donné
        return self.db.query(self.model).join(self.model.authors).filter(Author.name.ilike(f"%{author_name}%")).all()