from fastapi import FastAPI

from app.config import settings

from app.routes.contact import router as contact_router
from app.routes.newsletter import router as newsletter_router
from app.routes.inquiry import router as inquiry_router
from fastapi.middleware.cors import CORSMiddleware

from app.routes import career 

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "DigiScale API Running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://digiscale-gamma.vercel.app",
        "https://digiscaleinfotech.com",
        "https://www.digiscaleinfotech.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
from app.routes.contact import router as contact_router
from app.routes.newsletter import router as newsletter_router
from app.routes.inquiry import router as inquiry_router
app.include_router(career.router)

app.include_router(contact_router)
app.include_router(newsletter_router)
app.include_router(inquiry_router)