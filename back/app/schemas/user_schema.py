from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    username: str = Field(..., example="apéthy")
    email: EmailStr = Field(..., example="a.péthy@example.com")
    role: str = Field("user", example="admin")

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, example="p@ssw0rd")

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[str] = None

class UserOut(UserBase):
    id_user: int = Field(..., alias="id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
