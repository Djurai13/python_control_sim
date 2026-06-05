from uuid import UUID

from database.models.user import User

from database.repositories.user_repository import (
    UserRepository,
)

from services.security.password_service import (
    hash_password,
)


class UserService:

    def __init__(
        self,
        repository: UserRepository,
    ):
        self.repository = repository
        self.db = repository.db

    def create_user(
        self,
        username: str,
        email: str,
        password: str,
    ) -> User:

        if not username.strip():
            raise ValueError(
                "Username is required."
            )

        if not email.strip():
            raise ValueError(
                "Email is required."
            )

        if not password.strip():
            raise ValueError(
                "Password is required."
            )

        existing_user = (
            self.repository.get_by_username(
                username
            )
        )

        if existing_user:
            raise ValueError(
                "Username already exists."
            )

        existing_email = (
            self.repository.get_by_email(
                email
            )
        )

        if existing_email:
            raise ValueError(
                "Email already exists."
            )

        password_hash = hash_password(
            password
        )

        user = User(
            username=username,
            email=email,
            password_hash=password_hash,
        )

        try:
            self.repository.create(user)

            self.db.commit()

            self.db.refresh(user)

            return user

        except Exception:
            self.db.rollback()
            raise

    def get_user(
        self,
        user_id: UUID,
    ) -> User | None:
        return (
            self.repository.get_by_id(
                user_id
            )
        )

    def get_by_username(
        self,
        username: str,
    ) -> User | None:
        return (
            self.repository.get_by_username(
                username
            )
        )

    def get_by_email(
        self,
        email: str,
    ) -> User | None:
        return (
            self.repository.get_by_email(
                email
            )
        )

    def list_users(
        self,
    ) -> list[User]:
        return (
            self.repository.list_all()
        )

    def deactivate_user(
        self,
        user: User,
    ) -> User:

        try:
            user.is_active = False

            self.db.commit()

            self.db.refresh(user)

            return user

        except Exception:
            self.db.rollback()
            raise