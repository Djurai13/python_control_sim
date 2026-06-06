from pytest import raises

from services.validation.validation_rule import (
    ValidationRule,
)


def test_validation_rule_creation():

    rule = ValidationRule(
        name="username",
        rule_type="required",
    )

    assert rule.name == "username"

    assert rule.rule_type == "required"


def test_required_rule_pass():

    rule = ValidationRule(
        name="username",
        rule_type="required",
    )

    result = rule.validate(
        "john"
    )

    assert result["valid"] is True


def test_required_rule_fail():

    rule = ValidationRule(
        name="username",
        rule_type="required",
    )

    result = rule.validate(
        ""
    )

    assert result["valid"] is False


def test_min_length_pass():

    rule = ValidationRule(
        name="username",
        rule_type="min_length",
        rule_value=3,
    )

    result = rule.validate(
        "john"
    )

    assert result["valid"] is True


def test_min_length_fail():

    rule = ValidationRule(
        name="username",
        rule_type="min_length",
        rule_value=5,
    )

    result = rule.validate(
        "abc"
    )

    assert result["valid"] is False


def test_max_length_pass():

    rule = ValidationRule(
        name="username",
        rule_type="max_length",
        rule_value=10,
    )

    result = rule.validate(
        "john"
    )

    assert result["valid"] is True


def test_max_length_fail():

    rule = ValidationRule(
        name="username",
        rule_type="max_length",
        rule_value=3,
    )

    result = rule.validate(
        "john"
    )

    assert result["valid"] is False


def test_min_value_pass():

    rule = ValidationRule(
        name="age",
        rule_type="min_value",
        rule_value=18,
    )

    result = rule.validate(
        25
    )

    assert result["valid"] is True


def test_min_value_fail():

    rule = ValidationRule(
        name="age",
        rule_type="min_value",
        rule_value=18,
    )

    result = rule.validate(
        15
    )

    assert result["valid"] is False


def test_max_value_pass():

    rule = ValidationRule(
        name="age",
        rule_type="max_value",
        rule_value=65,
    )

    result = rule.validate(
        50
    )

    assert result["valid"] is True


def test_max_value_fail():

    rule = ValidationRule(
        name="age",
        rule_type="max_value",
        rule_value=65,
    )

    result = rule.validate(
        70
    )

    assert result["valid"] is False


def test_unsupported_rule_type():

    rule = ValidationRule(
        name="field",
        rule_type="invalid_rule",
    )

    with raises(
        ValueError
    ):
        rule.validate(
            "value"
        )