from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.controllers.serie_controller import SeriesController
from app.database.database import get_db

router = APIRouter()

@router.post("/")
def create_series(data: dict, db: Session = Depends(get_db)):
    return SeriesController(db).create_series(data)

@router.get("/{series_id}")
def get_series(series_id: int, db: Session = Depends(get_db)):
    series = SeriesController(db).get_series(series_id)
    if not series:
        raise HTTPException(status_code=404, detail="Série introuvable")
    return series

@router.get("/")
def get_all_series(db: Session = Depends(get_db)):
    return SeriesController(db).get_all_series()

@router.put("/{series_id}")
def update_series(series_id: int, data: dict, db: Session = Depends(get_db)):
    return SeriesController(db).update_series(series_id, data)

@router.delete("/{series_id}")
def delete_series(series_id: int, db: Session = Depends(get_db)):
    deleted = SeriesController(db).delete_series(series_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Série introuvable")
    return {"message": "Série supprimée."}