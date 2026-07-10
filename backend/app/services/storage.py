import uuid

from supabase import create_client

from app.config import (
    SUPABASE_URL,
    SUPABASE_SECRET_KEY,
    CAREER_BUCKET,
)

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY,
)

def upload_resume(file):

    extension = file.filename.split(".")[-1]

    filename = f"{uuid.uuid4()}.{extension}"

    data = file.file.read()

    supabase.storage.from_(CAREER_BUCKET).upload(
        path=filename,
        file=data,
        file_options={
            "content-type": file.content_type,
        },
    )

    return filename, file.filename
