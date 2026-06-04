from datetime import datetime
from uuid import UUID
from uuid import uuid4

from sqlalchemy import Boolean
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy.dialects.postgresql import UUID as PGUUID

from database.base import Base
from database.models.base_mixins import AuditMixin


class User(AuditMixin, Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
    PGUUID(as_uuid=True),
    primary_key=True,
    default=uuid4,
    )

    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    last_login: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )