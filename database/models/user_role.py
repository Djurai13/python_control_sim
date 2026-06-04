from uuid import UUID

from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy.dialects.postgresql import UUID as PGUUID

from database.base import Base


class UserRole(Base):
    __tablename__ = "user_roles"

    user_id: Mapped[UUID] = mapped_column(
     PGUUID(as_uuid=True),
    ForeignKey("users.id"),
    primary_key=True,
    )

    role_id: Mapped[UUID] = mapped_column(
         PGUUID(as_uuid=True),
        ForeignKey("roles.id"),
        primary_key=True,
    )