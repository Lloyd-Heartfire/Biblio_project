from pydantic import BaseModel, Field
from typing import Optional

class AuthorBase(BaseModel):
    name: str = Field(..., example="Victor Hugo")

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(BaseModel):
    name: Optional[str] = None

class AuthorOut(AuthorBase):
    id_author: int = Field(..., alias="id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
