from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict


class InquiryCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    company: str
    requirement: str
    project_details: str


class InquiryResponse(BaseModel):
    id: UUID
    full_name: str
    email: EmailStr
    phone: str
    company: str
    requirement: str
    project_details: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)