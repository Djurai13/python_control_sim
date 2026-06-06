from services.validation.validation_rule import (
    ValidationRule,
)

from services.validation.validation_service import (
    ValidationService,
)


def test_validation_service_creation():

    service = (
        ValidationService()
    )

    assert service is not None


def test_validate_field_success():

    service = (
        ValidationService()
    )

    rules = [
        ValidationRule(
            "username",
            "required",
        ),
        ValidationRule(
            "username",
            "min_length",
            3,
        ),
    ]

    result = (
        service.validate_field(
            "john",
            rules,
        )
    )

    assert (
        result["valid"]
        is True
    )

    assert (
        result["errors"]
        == []
    )


def test_validate_field_required_failure():

    service = (
        ValidationService()
    )

    rules = [
        ValidationRule(
            "username",
            "required",
        ),
    ]

    result = (
        service.validate_field(
            "",
            rules,
        )
    )

    assert (
        result["valid"]
        is False
    )

    assert (
        len(
            result[
                "errors"
            ]
        )
        == 1
    )


def test_validate_field_multiple_failures():

    service = (
        ValidationService()
    )

    rules = [
        ValidationRule(
            "username",
            "required",
        ),
        ValidationRule(
            "username",
            "min_length",
            5,
        ),
    ]

    result = (
        service.validate_field(
            "",
            rules,
        )
    )

    assert (
        result["valid"]
        is False
    )

    assert (
        len(
            result[
                "errors"
            ]
        )
        >= 1
    )


def test_validate_numeric_rules():

    service = (
        ValidationService()
    )

    rules = [
        ValidationRule(
            "age",
            "min_value",
            18,
        ),
        ValidationRule(
            "age",
            "max_value",
            65,
        ),
    ]

    result = (
        service.validate_field(
            30,
            rules,
        )
    )

    assert (
        result["valid"]
        is True
    )


def test_validate_numeric_failure():

    service = (
        ValidationService()
    )

    rules = [
        ValidationRule(
            "age",
            "min_value",
            18,
        ),
    ]

    result = (
        service.validate_field(
            15,
            rules,
        )
    )

    assert (
        result["valid"]
        is False
    )


def test_validate_without_rules():

    service = (
        ValidationService()
    )

    result = (
        service.validate_field(
            "value",
            [],
        )
    )

    assert (
        result["valid"]
        is True
    )

    assert (
        result["errors"]
        == []
    )