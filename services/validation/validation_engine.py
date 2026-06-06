from services.validation.validation_service import (
    ValidationService,
)

from services.validation.validation_rule import (
    ValidationRule,
)


class ValidationEngine:

    def __init__(
        self,
        validation_service: ValidationService,
    ) -> None:

        self.validation_service = (
            validation_service
        )

    def validate_record(
        self,
        record: dict,
        rules: dict[
            str,
            list[
                ValidationRule
            ]
        ],
    ) -> dict:

        errors = {}

        for (
            field_name,
            field_rules,
        ) in rules.items():

            value = record.get(
                field_name
            )

            result = (
                self.validation_service
                .validate_field(
                    value,
                    field_rules,
                )
            )

            if not result[
                "valid"
            ]:

                errors[
                    field_name
                ] = result[
                    "errors"
                ]

        return {
            "valid": (
                len(errors)
                == 0
            ),
            "errors": errors,
        }