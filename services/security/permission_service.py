from uuid import UUID

from database.models.permission import Permission

from database.repositories.permission_repository import (
    PermissionRepository,
)


class PermissionService:

    def __init__(
        self,
        repository: PermissionRepository,
    ):
        self.repository = repository

    def create_permission(
        self,
        permission_name: str,
        description: str | None = None,
    ) -> Permission:

        existing_permission = (
            self.repository.get_by_name(
                permission_name
            )
        )

        if existing_permission:
            raise ValueError(
                "Permission already exists."
            )

        permission = Permission(
            permission_name=permission_name,
            description=description,
        )

        self.repository.create(
            permission
        )

        return permission

    def get_permission(
        self,
        permission_id: UUID,
    ) -> Permission | None:
        return (
            self.repository.get_by_id(
                permission_id
            )
        )

    def list_permissions(
        self,
    ) -> list[Permission]:
        return (
            self.repository.list_all()
        )

    def delete_permission(
        self,
        permission: Permission,
    ) -> None:

        self.repository.delete(
            permission
        )