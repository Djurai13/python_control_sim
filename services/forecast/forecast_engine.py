from services.forecast.forecast_service import (
    ForecastService,
)


class ForecastEngine:

    def __init__(
        self,
        forecast_service: ForecastService,
    ) -> None:

        self.forecast_service = (
            forecast_service
        )

    def execute(
        self,
        forecast_name: str,
        forecast_period: int,
        base_value: float,
        growth_rate: float,
    ) -> dict:

        forecast = (
            self.forecast_service
            .create_forecast(
                forecast_name=
                forecast_name,

                forecast_period=
                forecast_period,

                base_value=
                base_value,
            )
        )

        projections = (
            self.forecast_service
            .project_linear_growth(
                base_value=
                base_value,

                growth_rate=
                growth_rate,

                periods=
                forecast_period,
            )
        )

        return {
            "forecast":
            forecast.to_dict(),

            "projections":
            projections,

            "status":
            "SUCCESS",
        }