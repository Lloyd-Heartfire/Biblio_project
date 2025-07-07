from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.controllers.author_controller import AuthorController
from app.database.database import get_db

router = APIRouter(
  prefix="/authors",
  tags=["authors"],
)

@router.post("/")
async def create_author(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    ctrl = AuthorController(db)
    user = ctrl.create_author(data)
    return {
            "id_author": user.id,
            "name": user.name,
        }

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