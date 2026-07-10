import uuid
from datetime import datetime

from sqlalchemy import String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Inquiry(Base):
    __tablename__ = "project_inquiries"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    full_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(150))
    phone: Mapped[str] = mapped_column(String(20))
    company: Mapped[str] = mapped_column(String(150))
    requirement: Mapped[str] = mapped_column(String(100))
    project_details: Mapped[str] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )