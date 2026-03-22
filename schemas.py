from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    # for POST required
    name:     str
    phone:    str
    email:    EmailStr
    password: str

class UserUpdate(BaseModel):
    # for PUT optional
    name:     Optional[str] = None
    phone:    Optional[str] = None
    email:    Optional[EmailStr] = None
    password: Optional[str] = None

class UserResponse(BaseModel):
    # in Response  password exclude
    id:    int
    name:  str
    phone: str
    email: str

    class Config:
        from_attributes = True  # ORM object → dict