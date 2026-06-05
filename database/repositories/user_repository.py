from uuid import UUID

from sqlalchemy.orm import Session

from database.models.user import User


class UserRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        user: User,
    ) -> User:
        self.db.add(user)

        return user

    def get_by_id(
        self,
        user_id: UUID,
    ) -> User | None:
        return (
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    def get_by_username(
        self,
        username: str,
    ) -> User | None:
        return (
            self.db.query(User)
            .filter(User.username == username)
            .first()
        )

    def get_by_email(
        self,
        email: str,
    ) -> User | None:
        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

    def list_all(
        self,
    ) -> list[User]:
        return (
            self.db.query(User)
            .order_by(User.username)
            .all()
        )

    def delete(
        self,
        user: User,
    ) -> None:
        self.db.delete(user)