from services.validation.validation_rule import (
    ValidationRule,
)

from services.validation.validation_service import (
    ValidationService,
)

from services.validation.validation_engine import (
    ValidationEngine,
)


def test_validation_engine_creation():

    service = (
        ValidationService()
    )

    engine = (
        ValidationEngine(
            service
        )
    )

    assert engine is not None


def test_validate_record_success():

    service = (
        ValidationService()
    )

    engine = (
        ValidationEngine(
            service
        )
    )

    record = {
        "username":
        "john",
        "age":
        30,
    }

    rules = {
        "username": [
            ValidationRule(
                "username",
                "required",
            ),
        ],
        "age": [
            ValidationRule(
                "age",
                "min_value",
                18,
            ),
        ],
    }

    result = (
        engine.validate_record(
            record,
            rules,
        )
    )

    assert (
        result["valid"]
        is True
    )

    assert (
        result["errors"]
        == {}
    )


def test_validate_record_failure():

    service = (
        ValidationService()
    )

    engine = (
        ValidationEngine(
            service
        )
    )

    record = {
        "username":
        "",
        "age":
        15,
    }

    rules = {
        "username": [
            ValidationRule(
                "username",
                "required",
            ),
        ],
        "age": [
            ValidationRule(
                "age",
                "min_value",
                18,
            ),
        ],
    }

    result = (
        engine.validate_record(
            record,
            rules,
        )
    )

    assert (
        result["valid"]
        is False
    )

    assert (
        "username"
        in result["errors"]
    )

    assert (
        "age"
        in result["errors"]
    )


def test_validate_partial_failure():

    service = (
        ValidationService()
    )

    engine = (
        ValidationEngine(
            service
        )
    )

    record = {
        "username":
        "john",
        "age":
        15,
    }

    rules = {
        "username": [
            ValidationRule(
                "username",
                "required",
            ),
        ],
        "age": [
            ValidationRule(
                "age",
                "min_value",
                18,
            ),
        ],
    }

    result = (
        engine.validate_record(
            record,
            rules,
        )
    )

    assert (
        result["valid"]
        is False
    )

    assert (
        "age"
        in result["errors"]
    )


def test_validate_empty_rules():

    service = (
        ValidationService()
    )

    engine = (
        ValidationEngine(
            service
        )
    )

    result = (
        engine.validate_record(
            {},
            {},
        )
    )

    assert (
        result["valid"]
        is True
    )

    assert (
        result["errors"]
        == {}
    )