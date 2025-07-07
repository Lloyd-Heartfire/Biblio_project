from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.controllers.serie_controller import SeriesController
from app.database.database import get_db

router = APIRouter(
  prefix="/series",
  tags=["series"],
)

@router.post("/")
async def create_series(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    ctrl = SeriesController(db)
    user = ctrl.create_series(data)
    return {
            "id_user": user.id,
            "name": user.name,
            "description": user.description,
        }

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