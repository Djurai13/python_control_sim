from services.quality.quality_service import (
    QualityService,
)


class QualityEngine:

    def __init__(
        self,
        quality_service: QualityService,
    ) -> None:

        self.quality_service = (
            quality_service
        )

    def assess_dataset(
        self,
        records: list[dict],
        total_records: int,
        valid_records: int,
    ) -> dict:

        completeness = (
            self.quality_service
            .assess_completeness(
                records
            )
        )

        validity = (
            self.quality_service
            .assess_validity(
                total_records,
                valid_records,
            )
        )

        overall_score = round(
            (
                completeness.score
                + validity.score
            )
            / 2,
            2,
        )

        return {
            "overall_score":
            overall_score,

            "completeness":
            completeness.to_dict(),

            "validity":
            validity.to_dict(),

            "passed":
            (
                completeness.passed
                and validity.passed
            ),
        }