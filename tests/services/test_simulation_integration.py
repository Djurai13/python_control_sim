from services.simulation.simulation_engine import (
    SimulationEngine,
)

from services.simulation.simulation_service import (
    SimulationService,
)


def build_engine():

    return SimulationEngine(
        SimulationService()
    )


def test_full_simulation_pipeline():

    engine = build_engine()

    result = engine.execute(
        simulation_name="forecast",
        parameters={
            "years": 5,
        },
    )

    assert result["result"]["status"] == "SUCCESS"

    assert result["run"]["status"] == "COMPLETED"


def test_simulation_metadata_preserved():

    engine = build_engine()

    result = engine.execute(
        simulation_name="population_growth",
        parameters={
            "population": 1000,
        },
    )

    assert (
        result["run"]
        ["simulation_name"]
        == "population_growth"
    )

    assert (
        result["run"]
        ["parameters"]
        ["population"]
        == 1000
    )


def test_created_at_exists():

    engine = build_engine()

    result = engine.execute(
        simulation_name="forecast",
        parameters={},
    )

    assert (
        result["run"]
        ["created_at"]
        is not None
    )


def test_multiple_simulations():

    engine = build_engine()

    first = engine.execute(
        "sim_a",
        {},
    )

    second = engine.execute(
        "sim_b",
        {},
    )

    assert (
        first["run"]
        ["simulation_name"]
        == "sim_a"
    )

    assert (
        second["run"]
        ["simulation_name"]
        == "sim_b"
    )


def test_result_structure():

    engine = build_engine()

    result = engine.execute(
        "forecast",
        {},
    )

    assert "run" in result

    assert "result" in result