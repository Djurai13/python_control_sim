from services.forecast.forecast_model import (
    ForecastModel,
)


def test_forecast_creation():

    forecast = (
        ForecastModel(
            forecast_name=
            "population",

            forecast_period=
            12,

            base_value=
            1000.0,
        )
    )

    assert (
        forecast.forecast_name
        == "population"
    )

    assert (
        forecast.forecast_period
        == 12
    )

    assert (
        forecast.base_value
        == 1000.0
    )


def test_forecast_to_dict():

    forecast = (
        ForecastModel(
            forecast_name=
            "demand",

            forecast_period=
            6,

            base_value=
            500.0,
        )
    )

    result = (
        forecast.to_dict()
    )

    assert (
        result[
            "forecast_name"
        ]
        == "demand"
    )

    assert (
        result[
            "forecast_period"
        ]
        == 6
    )

    assert (
        result[
            "base_value"
        ]
        == 500.0
    )


def test_forecast_timestamp_exists():

    forecast = (
        ForecastModel(
            forecast_name=
            "supply",

            forecast_period=
            3,

            base_value=
            100.0,
        )
    )

    assert (
        forecast.created_at
        is not None
    )


def test_forecast_name_preserved():

    forecast = (
        ForecastModel(
            forecast_name=
            "food_security",

            forecast_period=
            24,

            base_value=
            10000.0,
        )
    )

    assert (
        forecast.forecast_name
        == "food_security"
    )


def test_forecast_period_preserved():

    forecast = (
        ForecastModel(
            forecast_name=
            "water",

            forecast_period=
            18,

            base_value=
            2500.0,
        )
    )

    assert (
        forecast.forecast_period
        == 18
    )