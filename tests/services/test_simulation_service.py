import pytest

from services.simulation.simulation_service import (
    SimulationService,
)


def test_service_creation():

    service = (
        SimulationService()
    )

    assert service is not None


def test_create_run():

    service = (
        SimulationService()
    )

    run = (
        service.create_run(
            simulation_name=
            "forecast",

            parameters={
                "months": 12,
            },
        )
    )

    assert (
        run.simulation_name
        == "forecast"
    )

    assert (
        run.status
        == "PENDING"
    )


def test_reject_empty_name():

    service = (
        SimulationService()
    )

    with pytest.raises(
        ValueError
    ):

        service.create_run(
            simulation_name="",
            parameters={},
        )


def test_start_run():

    service = (
        SimulationService()
    )

    run = (
        service.create_run(
            "forecast",
            {},
        )
    )

    service.start_run(
        run
    )

    assert (
        run.status
        == "RUNNING"
    )


def test_complete_run():

    service = (
        SimulationService()
    )

    run = (
        service.create_run(
            "forecast",
            {},
        )
    )

    service.complete_run(
        run
    )

    assert (
        run.status
        == "COMPLETED"
    )


def test_fail_run():

    service = (
        SimulationService()
    )

    run = (
        service.create_run(
            "forecast",
            {},
        )
    )

    service.fail_run(
        run
    )

    assert (
        run.status
        == "FAILED"
    )