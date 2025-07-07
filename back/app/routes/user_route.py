from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.controllers.user_controller import UserController
from app.database.database import get_db

router = APIRouter(
  prefix="/users",
  tags=["users"],
)

@router.post("/")
async def create_user(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    ctrl = UserController(db)
    user = ctrl.create_user(data)
    return {
            "id_user": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        }

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