from unittest.mock import Mock

import pytest

from services.security.user_service import (
    UserService,
)


def test_user_service_creation():

    repository = Mock()

    repository.db = Mock()

    service = UserService(
        repository=repository,
    )

    assert service is not None


def test_create_user_rejects_duplicate_username():

    repository = Mock()

    repository.db = Mock()

    repository.get_by_username.return_value = (
        Mock()
    )

    service = UserService(
        repository=repository,
    )

    with pytest.raises(
        ValueError,
        match="Username already exists.",
    ):
        service.create_user(
            username="admin",
            email="admin@test.com",
            password="password",
        )


def test_create_user_rejects_duplicate_email():

    repository = Mock()

    repository.db = Mock()

    repository.get_by_username.return_value = (
        None
    )

    repository.get_by_email.return_value = (
        Mock()
    )

    service = UserService(
        repository=repository,
    )

    with pytest.raises(
        ValueError,
        match="Email already exists.",
    ):
        service.create_user(
            username="admin",
            email="admin@test.com",
            password="password",
        )


def test_create_user_rejects_empty_username():

    repository = Mock()

    repository.db = Mock()

    service = UserService(
        repository=repository,
    )

    with pytest.raises(
        ValueError,
        match="Username is required.",
    ):
        service.create_user(
            username="",
            email="admin@test.com",
            password="password",
        )


def test_create_user_rejects_empty_email():

    repository = Mock()

    repository.db = Mock()

    service = UserService(
        repository=repository,
    )

    with pytest.raises(
        ValueError,
        match="Email is required.",
    ):
        service.create_user(
            username="admin",
            email="",
            password="password",
        )


def test_create_user_rejects_empty_password():

    repository = Mock()

    repository.db = Mock()

    service = UserService(
        repository=repository,
    )

    with pytest.raises(
        ValueError,
        match="Password is required.",
    ):
        service.create_user(
            username="admin",
            email="admin@test.com",
            password="",
        )


def test_create_user_success():

    repository = Mock()

    repository.db = Mock()

    repository.get_by_username.return_value = (
        None
    )

    repository.get_by_email.return_value = (
        None
    )

    service = UserService(
        repository=repository,
    )

    user = service.create_user(
        username="admin",
        email="admin@test.com",
        password="password",
    )

    assert user.username == "admin"

    repository.create.assert_called_once()

    repository.db.commit.assert_called_once()

    repository.db.refresh.assert_called_once()


def test_deactivate_user():

    repository = Mock()

    repository.db = Mock()

    service = UserService(
        repository=repository,
    )

    user = Mock()

    user.is_active = True

    service.deactivate_user(
        user
    )

    assert user.is_active is False

    repository.db.commit.assert_called_once()

    repository.db.refresh.assert_called_once()


def test_create_user_rolls_back_on_failure():

    repository = Mock()

    repository.db = Mock()

    repository.get_by_username.return_value = (
        None
    )

    repository.get_by_email.return_value = (
        None
    )

    repository.create.side_effect = (
        Exception("Database failure")
    )

    service = UserService(
        repository=repository,
    )

    with pytest.raises(
        Exception,
        match="Database failure",
    ):
        service.create_user(
            username="admin",
            email="admin@test.com",
            password="password",
        )

    repository.db.rollback.assert_called_once()