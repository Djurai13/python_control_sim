from datetime import (
    datetime,
    UTC,
)


class ForecastModel:

    def __init__(
        self,
        forecast_name: str,
        forecast_period: int,
        base_value: float,
    ) -> None:

        self.forecast_name = (
            forecast_name
        )

        self.forecast_period = (
            forecast_period
        )

        self.base_value = (
            base_value
        )

        self.created_at = (
            datetime.now(
                UTC
            )
        )

    def to_dict(
        self,
    ) -> dict:

        return {
            "forecast_name":
                self.forecast_name,

            "forecast_period":
                self.forecast_period,

            "base_value":
                self.base_value,

            "created_at":
                self.created_at.isoformat(),
        }