from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict


class ContactCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    company: str
    service: str
    message: str


class ContactResponse(BaseModel):
    id: UUID
    full_name: str
    email: EmailStr
    phone: str
    company: str
    service: str
    message: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)