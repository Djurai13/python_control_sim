from uuid import UUID

from sqlalchemy.orm import Session

from database.models.role import Role


class RoleRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        role: Role,
    ) -> Role:
        self.db.add(role)

        return role

    def get_by_id(
        self,
        role_id: UUID,
    ) -> Role | None:
        return (
            self.db.query(Role)
            .filter(Role.id == role_id)
            .first()
        )

    def get_by_name(
        self,
        role_name: str,
    ) -> Role | None:
        return (
            self.db.query(Role)
            .filter(Role.role_name == role_name)
            .first()
        )

    def list_all(
        self,
    ) -> list[Role]:
        return (
            self.db.query(Role)
            .order_by(Role.role_name)
            .all()
        )

    def delete(
        self,
        role: Role,
    ) -> None:
        self.db.delete(role)