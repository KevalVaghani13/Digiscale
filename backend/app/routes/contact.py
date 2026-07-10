from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.contact import Contact
from app.schemas.contact import ContactCreate
from app.schemas.contact import ContactCreate, ContactResponse

router = APIRouter(
    prefix="/contact",
    tags=["Contact"],
)

@router.post("/")
def create_contact(
    contact: ContactCreate,
    db: Session = Depends(get_db),
):

    new_contact = Contact(
        full_name=contact.full_name,
        email=contact.email,
        phone=contact.phone,
        company=contact.company,
        service=contact.service,
        message=contact.message,
    )

    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)

    return {
        "success": True,
        "message": "Contact submitted successfully.",
        "data": new_contact,
    }

@router.get("/")
def get_contacts(
    db: Session = Depends(get_db),
):
    contacts = (
        db.query(Contact)
        .order_by(Contact.created_at.desc())
        .all()
    )

    return {
        "success": True,
        "count": len(contacts),
        "data": contacts,
    }

@router.get("/", response_model=list[ContactResponse])
def get_contacts(
    db: Session = Depends(get_db),
):
    contacts = (
        db.query(Contact)
        .order_by(Contact.created_at.desc())
        .all()
    )

    return contacts