from services.validation.validation_rule import (
    ValidationRule,
)


class ValidationService:

    def validate_field(
        self,
        value,
        rules: list[
            ValidationRule
        ],
    ) -> dict:

        errors = []

        for rule in rules:

            result = (
                rule.validate(
                    value
                )
            )

            if not result[
                "valid"
            ]:

                errors.append(
                    result[
                        "message"
                    ]
                )

        return {
            "valid": (
                len(errors)
                == 0
            ),
            "errors": errors,
        }