from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.models.base import Base
from app.models import Book, Image, User, Serie, Author

# URL de connexion
DATABASE_URL = "postgresql://postgres:password@db:5432/biblio"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

# conn=engine.connect()
# print(conn)
# result=conn.execute(text("select * from users"))
# print(result.fetchone())
# conn.commit()
def init_db():
    with engine.connect() as connection:
        connection.execute(text('''
            CREATE TABLE IF NOT EXISTS users (
                id_user SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL UNIQUE,
                email VARCHAR(255) NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role VARCHAR(255) NOT NULL
            );
        '''))
        connection.execute(text('''
            CREATE TABLE IF NOT EXISTS authors (
                id_author SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            );
        '''))
        connection.execute(text('''
            CREATE TABLE IF NOT EXISTS series (
                id_serie SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                created_at TIMESTAMP NOT NULL,
                description TEXT
            );
        '''))
        connection.execute(text('''
            CREATE TABLE IF NOT EXISTS images (
                id_image SERIAL PRIMARY KEY,
                url TEXT NOT NULL,
                name VARCHAR(255)
            );
        '''))
        connection.execute(text('''
            CREATE TABLE IF NOT EXISTS books (
                id_book SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                isbn VARCHAR(255),
                created_at TIMESTAMP NOT NULL,
                reading_status VARCHAR(255) NOT NULL,
                is_favorite BOOLEAN NOT NULL,
                description TEXT,
                id_serie INT REFERENCES series(id_serie)
            );
        '''))
        connection.execute(text('''
            CREATE TABLE IF NOT EXISTS user_books (
                id_user INT REFERENCES users(id_user),
                id_book INT REFERENCES books(id_book),
                PRIMARY KEY (id_user, id_book)
            );
        '''))
        connection.execute(text('''
            CREATE TABLE IF NOT EXISTS book_images (
                id_book INT REFERENCES books(id_book),
                id_image INT REFERENCES images(id_image),
                PRIMARY KEY (id_book, id_image)
            );
        '''))
        connection.execute(text('''
            CREATE TABLE IF NOT EXISTS author_books (
                id_author INT REFERENCES authors(id_author),
                id_book INT REFERENCES books(id_book),
                PRIMARY KEY (id_author, id_book)
            );
        '''))    

def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()