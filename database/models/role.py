from uuid import UUID
from uuid import uuid4

from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy.dialects.postgresql import UUID as PGUUID

from database.base import Base
from database.models.base_mixins import AuditMixin


class Role(AuditMixin, Base):
    __tablename__ = "roles"

    id: Mapped[UUID] = mapped_column(
    PGUUID(as_uuid=True),
    primary_key=True,
    default=uuid4,
    )

    role_name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )