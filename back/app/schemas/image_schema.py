from pydantic import BaseModel, Field, HttpUrl
from typing import Optional

class ImageBase(BaseModel):
    url: HttpUrl = Field(..., example="https://exemple.com/img.png")
    name: Optional[str] = Field(None, example="Couverture")

class ImageCreate(ImageBase):
    pass

class ImageUpdate(BaseModel):
    url: Optional[HttpUrl] = None
    name: Optional[str] = None

class ImageOut(ImageBase):
    id_image: int = Field(..., alias="id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
