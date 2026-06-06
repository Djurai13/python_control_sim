from datetime import (
    datetime,
    UTC,
)


class SimulationRun:

    def __init__(
        self,
        simulation_name: str,
        parameters: dict,
        status: str = "PENDING",
    ) -> None:

        self.simulation_name = (
            simulation_name
        )

        self.parameters = (
            parameters
        )

        self.status = status

        self.created_at = (
            datetime.now(
                UTC
            )
        )

    def mark_running(
        self,
    ) -> None:

        self.status = (
            "RUNNING"
        )

    def mark_completed(
        self,
    ) -> None:

        self.status = (
            "COMPLETED"
        )

    def mark_failed(
        self,
    ) -> None:

        self.status = (
            "FAILED"
        )

    def to_dict(
        self,
    ) -> dict:

        return {
            "simulation_name":
                self.simulation_name,

            "parameters":
                self.parameters,

            "status":
                self.status,

            "created_at":
                self.created_at.isoformat(),
        }