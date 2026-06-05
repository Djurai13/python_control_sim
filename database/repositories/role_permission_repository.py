from uuid import UUID

from sqlalchemy.orm import Session

from database.models.role_permission import RolePermission


class RolePermissionRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def assign_permission(
        self,
        role_id: UUID,
        permission_id: UUID,
    ) -> RolePermission:
        role_permission = RolePermission(
            role_id=role_id,
            permission_id=permission_id,
        )

        self.db.add(role_permission)

        return role_permission

    def get_assignment(
        self,
        role_id: UUID,
        permission_id: UUID,
    ) -> RolePermission | None:
        return (
            self.db.query(RolePermission)
            .filter(
                RolePermission.role_id == role_id,
                RolePermission.permission_id == permission_id,
            )
            .first()
        )

    def get_permissions_for_role(
        self,
        role_id: UUID,
    ) -> list[RolePermission]:
        return (
            self.db.query(RolePermission)
            .filter(RolePermission.role_id == role_id)
            .all()
        )

    def remove_assignment(
        self,
        assignment: RolePermission,
    ) -> None:
        self.db.delete(assignment)