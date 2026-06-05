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

    def create_user(
        self,
        username: str,
        email: str,
        password: str,
    ) -> User:

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

        self.repository.create(user)

        return user

    def get_user(
        self,
        user_id,
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

        user.is_active = False

        return user