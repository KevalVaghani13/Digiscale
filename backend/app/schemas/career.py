from pydantic import BaseModel, Field

class CareerApplicationCreate(BaseModel):

    first_name: str
    last_name: str

    email: str

    country_code: str = Field(..., min_length=2, max_length=10)

    phone: str = Field(..., min_length=6, max_length=15)

    experience: str

    location: str

    company: str | None = None

    role: str | None = None