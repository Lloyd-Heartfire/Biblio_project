from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers.image_controller import ImageController
from database import get_db

router = APIRouter()

@router.post("/")
def add_image(data: dict, db: Session = Depends(get_db)):
    return ImageController(db).add_image(data)

@router.get("/{image_id}")
def get_image(image_id: int, db: Session = Depends(get_db)):
    image = ImageController(db).get_image(image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Image introuvable")
    return image

@router.get("/")
def get_all_images(db: Session = Depends(get_db)):
    return ImageController(db).get_all_images()

@router.put("/{image_id}")
def update_image(image_id: int, data: dict, db: Session = Depends(get_db)):
    return ImageController(db).update_image(image_id, data)

@router.delete("/{image_id}")
def delete_image(image_id: int, db: Session = Depends(get_db)):
    deleted = ImageController(db).delete_image(image_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Image introuvable")
    return {"message": "Image supprimée."}