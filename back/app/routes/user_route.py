from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.controllers.user_controller import UserController
from app.database.database import get_db

router = APIRouter()

@router.post("/")
def create_user(data: dict, db: Session = Depends(get_db)):
    return UserController(db).create_user(data)

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = UserController(db).get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")
    return user

@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    return UserController(db).get_all_users()

@router.put("/{user_id}")
def update_user(user_id: int, data: dict, db: Session = Depends(get_db)):
    return UserController(db).update_user(user_id, data)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = UserController(db).delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")
    return {"message": "Utilisateur supprimé."}