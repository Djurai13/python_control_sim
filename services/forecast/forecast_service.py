from services.forecast.forecast_model import (
    ForecastModel,
)


class ForecastService:

    def create_forecast(
        self,
        forecast_name: str,
        forecast_period: int,
        base_value: float,
    ) -> ForecastModel:

        if not forecast_name:

            raise ValueError(
                "Forecast name is required."
            )

        if forecast_period <= 0:

            raise ValueError(
                "Forecast period must be greater than zero."
            )

        return ForecastModel(
            forecast_name=
            forecast_name,

            forecast_period=
            forecast_period,

            base_value=
            base_value,
        )

    def project_linear_growth(
        self,
        base_value: float,
        growth_rate: float,
        periods: int,
    ) -> list[float]:

        results = []

        current = base_value

        for _ in range(
            periods
        ):

            current = (
                current
                * (
                    1
                    + growth_rate
                )
            )

            results.append(
                round(
                    current,
                    2,
                )
            )

        return results