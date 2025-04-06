from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Optional[str] = "user"  # 👈 Campo opcional

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[str] = None  # 👈 Opcional también

class UserOut(BaseModel):
    id: UUID  # 👈 Aquí
    name: str
    email: EmailStr
    verified: bool
    role: str
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    is_active: bool

    class Config:
        from_attributes = True
