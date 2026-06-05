from uuid import UUID

from database.models.role import Role

from database.repositories.role_repository import (
    RoleRepository,
)


class RoleService:

    def __init__(
        self,
        repository: RoleRepository,
    ):
        self.repository = repository

    def create_role(
        self,
        role_name: str,
        description: str | None = None,
    ) -> Role:

        existing_role = (
            self.repository.get_by_name(
                role_name
            )
        )

        if existing_role:
            raise ValueError(
                "Role already exists."
            )

        role = Role(
            role_name=role_name,
            description=description,
        )

        self.repository.create(role)

        return role

    def get_role(
        self,
        role_id: UUID,
    ) -> Role | None:
        return (
            self.repository.get_by_id(
                role_id
            )
        )

    def list_roles(
        self,
    ) -> list[Role]:
        return (
            self.repository.list_all()
        )

    def delete_role(
        self,
        role: Role,
    ) -> None:

        self.repository.delete(
            role
        )