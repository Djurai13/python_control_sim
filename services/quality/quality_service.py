from services.quality.quality_assessment import (
    QualityAssessment,
)


class QualityService:

    def assess_completeness(
        self,
        records: list[dict],
    ) -> QualityAssessment:

        if not records:

            return QualityAssessment(
                dimension="completeness",
                score=0.0,
                passed=False,
            )

        total_fields = 0

        populated_fields = 0

        for record in records:

            for value in record.values():

                total_fields += 1

                if (
                    value is not None
                    and str(value).strip()
                    != ""
                ):
                    populated_fields += 1

        score = (
            populated_fields
            / total_fields
        ) * 100

        return QualityAssessment(
            dimension="completeness",
            score=round(
                score,
                2,
            ),
            passed=score >= 80,
        )

    def assess_validity(
        self,
        total_records: int,
        valid_records: int,
    ) -> QualityAssessment:

        if total_records <= 0:

            return QualityAssessment(
                dimension="validity",
                score=0.0,
                passed=False,
            )

        score = (
            valid_records
            / total_records
        ) * 100

        return QualityAssessment(
            dimension="validity",
            score=round(
                score,
                2,
            ),
            passed=score >= 80,
        )