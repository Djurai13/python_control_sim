import pytest

from services.forecast.forecast_service import (
    ForecastService,
)


def test_service_creation():

    service = (
        ForecastService()
    )

    assert service is not None


def test_create_forecast():

    service = (
        ForecastService()
    )

    forecast = (
        service.create_forecast(
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


def test_reject_empty_name():

    service = (
        ForecastService()
    )

    with pytest.raises(
        ValueError
    ):

        service.create_forecast(
            forecast_name="",
            forecast_period=12,
            base_value=100,
        )


def test_reject_invalid_period():

    service = (
        ForecastService()
    )

    with pytest.raises(
        ValueError
    ):

        service.create_forecast(
            forecast_name=
            "population",

            forecast_period=0,

            base_value=100,
        )


def test_linear_growth_projection():

    service = (
        ForecastService()
    )

    results = (
        service.project_linear_growth(
            base_value=100,

            growth_rate=0.10,

            periods=3,
        )
    )

    assert (
        results
        ==
        [
            110.0,
            121.0,
            133.1,
        ]
    )


def test_projection_length():

    service = (
        ForecastService()
    )

    results = (
        service.project_linear_growth(
            base_value=100,

            growth_rate=0.05,

            periods=5,
        )
    )

    assert (
        len(results)
        == 5
    )