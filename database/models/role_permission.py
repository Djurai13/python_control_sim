from uuid import UUID

from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy.dialects.postgresql import UUID as PGUUID

from database.base import Base


class RolePermission(Base):
    __tablename__ = "role_permissions"

    role_id: Mapped[UUID] = mapped_column(
    PGUUID(as_uuid=True),
    ForeignKey("roles.id"),
    primary_key=True,
    )

    permission_id: Mapped[UUID] = mapped_column(
    PGUUID(as_uuid=True),
    ForeignKey("permissions.id"),
    primary_key=True,
    )