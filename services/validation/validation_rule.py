class ValidationRule:

    def __init__(
        self,
        name: str,
        rule_type: str,
        rule_value=None,
    ) -> None:

        self.name = name
        self.rule_type = rule_type
        self.rule_value = rule_value

    def validate(
        self,
        value,
    ) -> dict:

        if self.rule_type == "required":

            if value is None:
                return {
                    "valid": False,
                    "message": (
                        f"{self.name} "
                        "is required."
                    ),
                }

            if (
                isinstance(
                    value,
                    str,
                )
                and not value.strip()
            ):
                return {
                    "valid": False,
                    "message": (
                        f"{self.name} "
                        "is required."
                    ),
                }

            return {
                "valid": True,
                "message": None,
            }

        if (
            self.rule_type
            == "min_length"
        ):

            if (
                len(value)
                < self.rule_value
            ):
                return {
                    "valid": False,
                    "message": (
                        f"{self.name} "
                        f"must be at least "
                        f"{self.rule_value} "
                        "characters."
                    ),
                }

            return {
                "valid": True,
                "message": None,
            }

        if (
            self.rule_type
            == "max_length"
        ):

            if (
                len(value)
                > self.rule_value
            ):
                return {
                    "valid": False,
                    "message": (
                        f"{self.name} "
                        f"must not exceed "
                        f"{self.rule_value} "
                        "characters."
                    ),
                }

            return {
                "valid": True,
                "message": None,
            }

        if (
            self.rule_type
            == "min_value"
        ):

            if (
                value
                < self.rule_value
            ):
                return {
                    "valid": False,
                    "message": (
                        f"{self.name} "
                        f"must be at least "
                        f"{self.rule_value}."
                    ),
                }

            return {
                "valid": True,
                "message": None,
            }

        if (
            self.rule_type
            == "max_value"
        ):

            if (
                value
                > self.rule_value
            ):
                return {
                    "valid": False,
                    "message": (
                        f"{self.name} "
                        f"must not exceed "
                        f"{self.rule_value}."
                    ),
                }

            return {
                "valid": True,
                "message": None,
            }

        raise ValueError(
            "Unsupported rule type."
        )