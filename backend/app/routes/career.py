from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.career import CareerApplication
from app.services.storage import upload_resume

router = APIRouter(
    prefix="/career",
    tags=["Career"],
)


@router.post("/")
async def submit_application(

    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),

    country_code: str = Form(...),
    phone: str = Form(...),

    experience: str = Form(...),
    location: str = Form(...),

    company: str = Form(""),
    role: str = Form(""),

    job_title: str = Form(...),

    resume: UploadFile = File(...),

    db: Session = Depends(get_db),
):
    
    try:

        # Upload Resume to Supabase Storage
        resume_filename, original_resume_name = upload_resume(resume)

        # Save Application
        application = CareerApplication(

        first_name=first_name,
        last_name=last_name,
        email=email,

        country_code=country_code,
        phone=phone,

        experience=experience,
        location=location,

        company=company,
        role=role,

        job_title=job_title,
        status="Pending",

        resume_file=resume_filename,
        resume_original_name=original_resume_name,
    
        )

        db.add(application)
        db.commit()
        db.refresh(application)

        return {
            "success": True,
            "message": "Application submitted successfully.",
            "application_id": str(application.id),
        }

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )