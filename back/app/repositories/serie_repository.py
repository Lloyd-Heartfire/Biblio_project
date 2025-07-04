from sqlalchemy.orm import Session
from models.serie import Serie
from .base import BaseRepository

class SerieRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, Serie)

    def get_all(self):
        return self.db.query(self.model).all()

    def get_by_name(self, name: str):
        return self.db.query(self.model).filter_by(name=name).first()
    
    def get_books(self, id_serie: int):
        series = self.get(id_serie)
        return series.books if series else []