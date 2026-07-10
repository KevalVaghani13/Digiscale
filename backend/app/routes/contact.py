from fastapi import APIRouter, HTTPException
from app.supabase_client import supabase
from app.schemas.contact import ContactCreate, ContactResponse

router = APIRouter(
    prefix="/contact",
    tags=["Contact"],
)

@router.post("/")
def create_contact(
    contact: ContactCreate,
):
    insert_response = (
        supabase.table("contact_messages")
        .insert({
            "full_name": contact.full_name,
            "email": contact.email,
            "phone": contact.phone,
            "company": contact.company,
            "service": contact.service,
            "message": contact.message,
        })
        .execute()
    )

    if not insert_response.data:
        raise HTTPException(
            status_code=500,
            detail="Failed to submit contact message."
        )

    return {
        "success": True,
        "message": "Contact submitted successfully.",
        "data": insert_response.data[0],
    }

@router.get("/")
def get_contacts():
    response = (
        supabase.table("contact_messages")
        .select("*")
        .order("created_at", descending=True)
        .execute()
    )

    contacts = response.data if response.data else []

    return {
        "success": True,
        "count": len(contacts),
        "data": contacts,
    }

@router.get("/", response_model=list[ContactResponse])
def get_contacts_list():
    response = (
        supabase.table("contact_messages")
        .select("*")
        .order("created_at", descending=True)
        .execute()
    )

    contacts = response.data if response.data else []
    return contacts