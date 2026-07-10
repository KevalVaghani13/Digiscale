from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.inquiry import Inquiry
from app.schemas.inquiry import (
    InquiryCreate,
    InquiryResponse,
)

router = APIRouter(
    prefix="/inquiry",
    tags=["Inquiry"],
)


@router.post("/", response_model=InquiryResponse)
def create_inquiry(
    inquiry: InquiryCreate,
    db: Session = Depends(get_db),
):

    new_inquiry = Inquiry(
        full_name=inquiry.full_name,
        email=inquiry.email,
        phone=inquiry.phone,
        company=inquiry.company,
        requirement=inquiry.requirement,
        project_details=inquiry.project_details,
    )

    db.add(new_inquiry)
    db.commit()
    db.refresh(new_inquiry)

    return new_inquiry