from fastapi import APIRouter, HTTPException
from app.supabase_client import supabase
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
):
    # Query supabase
    response = (
        supabase.table("newsletter_subscribers")
        .select("*")
        .eq("email", newsletter.email)
        .execute()
    )

    if response.data:
        raise HTTPException(
            status_code=409,
            detail="Email already subscribed."
        )

    # Insert subscriber
    insert_response = (
        supabase.table("newsletter_subscribers")
        .insert({"email": newsletter.email})
        .execute()
    )

    if not insert_response.data:
        raise HTTPException(
            status_code=500,
            detail="Failed to subscribe email."
        )

    return insert_response.data[0]