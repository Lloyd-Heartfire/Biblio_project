from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers.author_controller import AuthorController
from database import get_db

router = APIRouter()

@router.post("/")
def create_author(data: dict, db: Session = Depends(get_db)):
    return AuthorController(db).create_author(data)

@router.get("/{author_id}")
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = AuthorController(db).get_author(author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Auteur introuvable")
    return author

@router.get("/")
def get_all_authors(db: Session = Depends(get_db)):
    return AuthorController(db).get_all_authors()

@router.put("/{author_id}")
def update_author(author_id: int, data: dict, db: Session = Depends(get_db)):
    return AuthorController(db).update_author(author_id, data)

@router.delete("/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    deleted = AuthorController(db).delete_author(author_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Auteur introuvable")
    return {"message": "Auteur supprimé."}