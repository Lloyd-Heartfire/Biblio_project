from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

# Table de relation entre les livres et les auteurs
author_books = Table(
    "author_books",
    Base.metadata,
    Column("id_author", Integer, ForeignKey("authors.id_author"), primary_key=True),
    Column("id_book", Integer, ForeignKey("books.id_book"), primary_key=True),
)

# Table de relation entre les livres et les utilisateurs
user_books = Table(
    "user_books",
    Base.metadata,
    Column("id_user", Integer, ForeignKey("users.id_user"), primary_key=True),
    Column("id_book", Integer, ForeignKey("books.id_book"), primary_key=True),
)

# Table de relation entre les livres et les images
book_images = Table(
    "book_images",
    Base.metadata,
    Column("id_book", Integer, ForeignKey("books.id_book"), primary_key=True),
    Column("id_image", Integer, ForeignKey("images.id_image"), primary_key=True),
)