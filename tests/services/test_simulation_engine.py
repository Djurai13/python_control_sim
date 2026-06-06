from services.simulation.simulation_engine import (
    SimulationEngine,
)

from services.simulation.simulation_service import (
    SimulationService,
)


def test_engine_creation():

    engine = (
        SimulationEngine(
            SimulationService()
        )
    )

    assert engine is not None


def test_execute_simulation():

    engine = (
        SimulationEngine(
            SimulationService()
        )
    )

    result = (
        engine.execute(
            simulation_name=
            "forecast",

            parameters={
                "months": 12,
            },
        )
    )

    assert (
        result["result"]
        ["status"]
        == "SUCCESS"
    )

    assert (
        result["run"]
        ["status"]
        == "COMPLETED"
    )


def test_simulation_name_preserved():

    engine = (
        SimulationEngine(
            SimulationService()
        )
    )

    result = (
        engine.execute(
            "population_growth",
            {},
        )
    )

    assert (
        result["run"]
        ["simulation_name"]
        == "population_growth"
    )


def test_parameters_preserved():

    engine = (
        SimulationEngine(
            SimulationService()
        )
    )

    result = (
        engine.execute(
            "forecast",
            {
                "years": 5,
            },
        )
    )

    assert (
        result["run"]
        ["parameters"]
        ["years"]
        == 5
    )


def test_execution_returns_result():

    engine = (
        SimulationEngine(
            SimulationService()
        )
    )

    result = (
        engine.execute(
            "forecast",
            {},
        )
    )

    assert (
        "result"
        in result
    )

    assert (
        "run"
        in result
    )