from services.forecast.forecast_engine import (
    ForecastEngine,
)

from services.forecast.forecast_service import (
    ForecastService,
)


def test_engine_creation():

    engine = (
        ForecastEngine(
            ForecastService()
        )
    )

    assert engine is not None


def test_execute_forecast():

    engine = (
        ForecastEngine(
            ForecastService()
        )
    )

    result = (
        engine.execute(
            forecast_name=
            "population",

            forecast_period=
            3,

            base_value=
            100,

            growth_rate=
            0.10,
        )
    )

    assert (
        result["status"]
        == "SUCCESS"
    )


def test_projection_count():

    engine = (
        ForecastEngine(
            ForecastService()
        )
    )

    result = (
        engine.execute(
            forecast_name=
            "population",

            forecast_period=
            5,

            base_value=
            100,

            growth_rate=
            0.05,
        )
    )

    assert (
        len(
            result[
                "projections"
            ]
        )
        == 5
    )


def test_forecast_metadata():

    engine = (
        ForecastEngine(
            ForecastService()
        )
    )

    result = (
        engine.execute(
            forecast_name=
            "food_security",

            forecast_period=
            2,

            base_value=
            500,

            growth_rate=
            0.02,
        )
    )

    assert (
        result["forecast"]
        ["forecast_name"]
        == "food_security"
    )


def test_projection_values():

    engine = (
        ForecastEngine(
            ForecastService()
        )
    )

    result = (
        engine.execute(
            forecast_name=
            "demand",

            forecast_period=
            3,

            base_value=
            100,

            growth_rate=
            0.10,
        )
    )

    assert (
        result[
            "projections"
        ]
        ==
        [
            110.0,
            121.0,
            133.1,
        ]
    )