from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class SerieBase(BaseModel):
    name: str = Field(..., example="La croisée des mondes")
    description: Optional[str] = Field(None, example="Saga de je ne sais plus quoi mais fantastique en tout cas")

class SerieCreate(SerieBase):
    pass

class SerieUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class SerieOut(SerieBase):
    id_serie: int = Field(..., alias="id")
    created_at: datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
