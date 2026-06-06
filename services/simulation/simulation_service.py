from services.simulation.simulation_run import (
    SimulationRun,
)


class SimulationService:

    def create_run(
        self,
        simulation_name: str,
        parameters: dict,
    ) -> SimulationRun:

        if not simulation_name:

            raise ValueError(
                "Simulation name is required."
            )

        return SimulationRun(
            simulation_name=
            simulation_name,

            parameters=
            parameters,
        )

    def start_run(
        self,
        run: SimulationRun,
    ) -> SimulationRun:

        run.mark_running()

        return run

    def complete_run(
        self,
        run: SimulationRun,
    ) -> SimulationRun:

        run.mark_completed()

        return run

    def fail_run(
        self,
        run: SimulationRun,
    ) -> SimulationRun:

        run.mark_failed()

        return run