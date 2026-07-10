import uuid
from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class CareerApplication(Base):
    __tablename__ = "career_applications"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    country_code: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        default="+91",
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    experience: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    location: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    company: Mapped[str] = mapped_column(
        String(150),
        nullable=True,
    )

    role: Mapped[str] = mapped_column(
        String(150),
        nullable=True,
    )

    job_title: Mapped[str] = mapped_column(
    String(150),
    nullable=False,
    )

    resume_file: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    resume_original_name: Mapped[str] = mapped_column(
    String(255),
    nullable=False,
    )

    status: Mapped[str] = mapped_column(
    String(50),
    nullable=False,
    default="Pending",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )