from services.simulation.simulation_service import (
    SimulationService,
)


class SimulationEngine:

    def __init__(
        self,
        simulation_service: SimulationService,
    ) -> None:

        self.simulation_service = (
            simulation_service
        )

    def execute(
        self,
        simulation_name: str,
        parameters: dict,
    ) -> dict:

        run = (
            self.simulation_service
            .create_run(
                simulation_name,
                parameters,
            )
        )

        self.simulation_service.start_run(
            run
        )

        try:

            result = {
                "simulation":
                simulation_name,

                "parameters":
                parameters,

                "status":
                "SUCCESS",
            }

            self.simulation_service.complete_run(
                run
            )

            return {
                "run":
                run.to_dict(),

                "result":
                result,
            }

        except Exception:

            self.simulation_service.fail_run(
                run
            )

            raise