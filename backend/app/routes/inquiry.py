from fastapi import APIRouter, HTTPException
from app.supabase_client import supabase
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
):
    insert_response = (
        supabase.table("project_inquiries")
        .insert({
            "full_name": inquiry.full_name,
            "email": inquiry.email,
            "phone": inquiry.phone,
            "company": inquiry.company,
            "requirement": inquiry.requirement,
            "project_details": inquiry.project_details,
        })
        .execute()
    )

    if not insert_response.data:
        raise HTTPException(
            status_code=500,
            detail="Failed to create project inquiry."
        )

    return insert_response.data[0]