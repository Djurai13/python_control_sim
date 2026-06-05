from uuid import UUID

from sqlalchemy.orm import Session

from database.models.permission import Permission


class PermissionRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        permission: Permission,
    ) -> Permission:
        self.db.add(permission)

        return permission

    def get_by_id(
        self,
        permission_id: UUID,
    ) -> Permission | None:
        return (
            self.db.query(Permission)
            .filter(Permission.id == permission_id)
            .first()
        )

    def get_by_name(
        self,
        permission_name: str,
    ) -> Permission | None:
        return (
            self.db.query(Permission)
            .filter(
                Permission.permission_name == permission_name
            )
            .first()
        )

    def list_all(
        self,
    ) -> list[Permission]:
        return (
            self.db.query(Permission)
            .order_by(Permission.permission_name)
            .all()
        )

    def delete(
        self,
        permission: Permission,
    ) -> None:
        self.db.delete(permission)