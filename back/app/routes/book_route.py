from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers.book_controller import BookController
from database import get_db

router = APIRouter()

@router.post("/")
def create_book(data: dict, db: Session = Depends(get_db)):
    return BookController(db).create_book(data)

@router.get("/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = BookController(db).get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Livre introuvable")
    return book

@router.get("/")
def get_all_books(db: Session = Depends(get_db)):
    return BookController(db).get_all_books()

@router.put("/{book_id}")
def update_book(book_id: int, data: dict, db: Session = Depends(get_db)):
    return BookController(db).update_book(book_id, data)

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted = BookController(db).delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Livre introuvable")
    return {"message": "Livre supprimé."}