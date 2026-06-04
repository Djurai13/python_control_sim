from sqlalchemy import DateTime
from uuid import UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from datetime import datetime


class AuditMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    created_by: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
    )

    updated_by: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
    )