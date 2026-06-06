from services.forecast.forecast_engine import (
    ForecastEngine,
)

from services.forecast.forecast_service import (
    ForecastService,
)


def build_engine():

    return ForecastEngine(
        ForecastService()
    )


def test_full_forecast_pipeline():

    engine = build_engine()

    result = engine.execute(
        forecast_name="population",
        forecast_period=3,
        base_value=100,
        growth_rate=0.10,
    )

    assert result["status"] == "SUCCESS"

    assert (
        result["projections"]
        ==
        [
            110.0,
            121.0,
            133.1,
        ]
    )


def test_forecast_metadata_preserved():

    engine = build_engine()

    result = engine.execute(
        forecast_name="food_security",
        forecast_period=2,
        base_value=500,
        growth_rate=0.02,
    )

    assert (
        result["forecast"]
        ["forecast_name"]
        == "food_security"
    )


def test_projection_length():

    engine = build_engine()

    result = engine.execute(
        forecast_name="water",
        forecast_period=5,
        base_value=100,
        growth_rate=0.05,
    )

    assert (
        len(
            result["projections"]
        )
        == 5
    )


def test_timestamp_exists():

    engine = build_engine()

    result = engine.execute(
        forecast_name="demand",
        forecast_period=1,
        base_value=100,
        growth_rate=0.10,
    )

    assert (
        result["forecast"]
        ["created_at"]
        is not None
    )


def test_result_structure():

    engine = build_engine()

    result = engine.execute(
        forecast_name="forecast",
        forecast_period=1,
        base_value=100,
        growth_rate=0.10,
    )

    assert "forecast" in result

    assert "projections" in result

    assert "status" in result