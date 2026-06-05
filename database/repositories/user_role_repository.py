from uuid import UUID

from sqlalchemy.orm import Session

from database.models.user_role import UserRole


class UserRoleRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def assign_role(
        self,
        user_id: UUID,
        role_id: UUID,
    ) -> UserRole:
        user_role = UserRole(
            user_id=user_id,
            role_id=role_id,
        )

        self.db.add(user_role)

        return user_role

    def get_assignment(
        self,
        user_id: UUID,
        role_id: UUID,
    ) -> UserRole | None:
        return (
            self.db.query(UserRole)
            .filter(
                UserRole.user_id == user_id,
                UserRole.role_id == role_id,
            )
            .first()
        )

    def get_roles_for_user(
        self,
        user_id: UUID,
    ) -> list[UserRole]:
        return (
            self.db.query(UserRole)
            .filter(UserRole.user_id == user_id)
            .all()
        )

    def remove_assignment(
        self,
        assignment: UserRole,
    ) -> None:
        self.db.delete(assignment)