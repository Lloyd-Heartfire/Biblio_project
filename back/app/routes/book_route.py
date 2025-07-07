from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.controllers.book_controller import BookController
from app.database.database import get_db

router = APIRouter(
  prefix="/books",
  tags=["books"],
)

@router.post("/")
async def create_book(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    ctrl = BookController(db)
    user = ctrl.create_book(data)
    return {
            "id_book": user.id,
            "title": user.title,
            "isbn": user.isbn,
            "reading_status": user.reading_status,
            "is_favorite": user.is_favorite,
            "description": user.description,
        }

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