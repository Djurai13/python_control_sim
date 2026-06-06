from services.simulation.simulation_run import (
    SimulationRun,
)


def test_simulation_run_creation():

    run = (
        SimulationRun(
            simulation_name="test",
            parameters={
                "population": 100,
            },
        )
    )

    assert (
        run.simulation_name
        == "test"
    )

    assert (
        run.parameters[
            "population"
        ]
        == 100
    )

    assert (
        run.status
        == "PENDING"
    )


def test_mark_running():

    run = (
        SimulationRun(
            simulation_name="test",
            parameters={},
        )
    )

    run.mark_running()

    assert (
        run.status
        == "RUNNING"
    )


def test_mark_completed():

    run = (
        SimulationRun(
            simulation_name="test",
            parameters={},
        )
    )

    run.mark_completed()

    assert (
        run.status
        == "COMPLETED"
    )


def test_mark_failed():

    run = (
        SimulationRun(
            simulation_name="test",
            parameters={},
        )
    )

    run.mark_failed()

    assert (
        run.status
        == "FAILED"
    )


def test_to_dict():

    run = (
        SimulationRun(
            simulation_name="forecast",
            parameters={
                "months": 12,
            },
        )
    )

    result = (
        run.to_dict()
    )

    assert (
        result[
            "simulation_name"
        ]
        == "forecast"
    )

    assert (
        result[
            "parameters"
        ]["months"]
        == 12
    )

    assert (
        result[
            "status"
        ]
        == "PENDING"
    )