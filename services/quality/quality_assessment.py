class QualityAssessment:

    def __init__(
        self,
        dimension: str,
        score: float,
        passed: bool,
    ) -> None:

        self.dimension = dimension

        self.score = score

        self.passed = passed

    def to_dict(
        self,
    ) -> dict:

        return {
            "dimension":
            self.dimension,

            "score":
            self.score,

            "passed":
            self.passed,
        }