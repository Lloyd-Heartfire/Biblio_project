from repositories.serie_repository import SerieRepository
from sqlalchemy.orm import Session

class SeriesController:
    def __init__(self, db: Session):
        self.repo = SerieRepository(db)

    def create_series(self, data: dict):
        return self.repo.create(data)
    
    def get_series(self, series_id: int):
        return self.repo.get(series_id)

    def get_all_series(self):
        return self.repo.get_all()

    def update_series(self, series_id: int, data: dict):
        return self.repo.update(series_id, data)

    def delete_series(self, series_id: int):
        series = self.repo.get(series_id)
        if series:
            self.repo.delete(series_id)
        return series

    def search_by_name(self, name: str):
        return self.repo.get_by_name(name)

    def list_books(self, series_id: int):
        return self.repo.get_books(series_id)