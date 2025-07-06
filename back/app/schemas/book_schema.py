# from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# class ReadingStatus(str, Enum):
#     a_lire = "a lire"
#     en_cours = "en cours"
#     lu = "lu"

# Classe de base pour les livres, partagée par Create, Update et Out
class BookBase(BaseModel):
    title: str = Field(..., example="C'est un titre de livre")
    isbn: Optional[str] = Field(None, example="999-1234567890")
    # reading_status: ReadingStatus = Field(
    #     ReadingStatus.a_lire, example=ReadingStatus.en_cours
    # )
    is_favorite: bool = Field(False, example=True)
    description: Optional[str] = Field(None, example="Une histoire à chier, n'achetez pas ce livre…")
    id_serie: Optional[int] = Field(None, example=1)

# Schéma utilisé lors de la création d'un livre
# Hérite de BookBase, donc pas besoin d'ajouts de champs
class BookCreate(BookBase):
    pass

# Schéma pour la mise à jour d'un livre
class BookUpdate(BaseModel):
    title: Optional[str] = None
    isbn: Optional[str] = None
    # reading_status: Optional[ReadingStatus] = None
    is_favorite: Optional[bool] = None
    description: Optional[str] = None
    id_serie: Optional[int] = None

# Schéma de sortie pour un livre, utilisé pour les réponses API
class BookOut(BookBase):
    id_book: int = Field(..., alias="id")
    created_at: datetime

    # Permet d'utiliser les alias et la compatibilité avec l'ORM
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
