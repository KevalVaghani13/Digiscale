from supabase import create_client
from app.config import settings

print("SUPABASE_URL =", repr(settings.SUPABASE_URL))

supabase = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_SECRET_KEY,
)