-- Création du type ENUM pour reading_status
CREATE TYPE reading_status_enum AS ENUM ('à_lire', 'en_cours', 'lu');

CREATE TABLE users (
    id_user SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role VARCHAR(255) NOT NULL
);

CREATE TABLE authors (
    id_author SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE series (
    id_serie SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    description TEXT
);

CREATE TABLE images (
    id_image SERIAL PRIMARY KEY,
    url TEXT NOT NULL,
    name VARCHAR(255)
);

CREATE TABLE books (
    id_book SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    isbn VACHAR(255),
    created_at TIMESTAMP NOT NULL,
    reading_status reading_status_enum NOT NULL,
    is_favorite BOOLEAN NOT NULL,
    description TEXT,
    id_serie INT REFERENCES series(id_serie)
);

CREATE TABLE user_books (
    id_user INT REFERENCES users(id_user),
    id_book INT REFERENCES books(id_book),
    PRIMARY KEY (id_user, id_book)
);

CREATE TABLE book_images (
    id_book INT REFERENCES books(id_book),
    id_image INT REFERENCES images(id_image),
    PRIMARY KEY (id_book, id_image)
);

CREATE TABLE author_books (
    id_author INT REFERENCES authors(id_author),
    id_book INT REFERENCES books(id_book),
    PRIMARY KEY (id_author, id_book)
);