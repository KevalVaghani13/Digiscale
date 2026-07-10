from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.supabase_client import supabase
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
):
    try:
        # Upload Resume to Supabase Storage
        resume_filename, original_resume_name = upload_resume(resume)

        # Save Application
        insert_response = (
            supabase.table("career_applications")
            .insert({
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "country_code": country_code,
                "phone": phone,
                "experience": experience,
                "location": location,
                "company": company,
                "role": role,
                "job_title": job_title,
                "status": "Pending",
                "resume_file": resume_filename,
                "resume_original_name": original_resume_name,
            })
            .execute()
        )

        if not insert_response.data:
            raise HTTPException(
                status_code=500,
                detail="Failed to save career application."
            )

        application = insert_response.data[0]

        return {
            "success": True,
            "message": "Application submitted successfully.",
            "application_id": str(application.get("id")),
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )