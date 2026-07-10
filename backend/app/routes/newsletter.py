from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.newsletter import Newsletter
from app.schemas.newsletter import (
    NewsletterCreate,
    NewsletterResponse,
)

router = APIRouter(
    prefix="/newsletter",
    tags=["Newsletter"],
)

@router.post("/", response_model=NewsletterResponse)
def subscribe_newsletter(
    newsletter: NewsletterCreate,
    db: Session = Depends(get_db),
):
    existing = (
        db.query(Newsletter)
        .filter(Newsletter.email == newsletter.email)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Email already subscribed."
        )

    new_subscriber = Newsletter(
        email=newsletter.email,
    )

    db.add(new_subscriber)
    db.commit()
    db.refresh(new_subscriber)

    return new_subscriber