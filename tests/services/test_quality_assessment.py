from services.quality.quality_assessment import (
    QualityAssessment,
)


def test_quality_assessment_creation():

    assessment = (
        QualityAssessment(
            dimension="completeness",
            score=100.0,
            passed=True,
        )
    )

    assert (
        assessment.dimension
        == "completeness"
    )

    assert (
        assessment.score
        == 100.0
    )

    assert (
        assessment.passed
        is True
    )


def test_quality_assessment_to_dict():

    assessment = (
        QualityAssessment(
            dimension="validity",
            score=95.5,
            passed=True,
        )
    )

    result = (
        assessment.to_dict()
    )

    assert (
        result["dimension"]
        == "validity"
    )

    assert (
        result["score"]
        == 95.5
    )

    assert (
        result["passed"]
        is True
    )


def test_quality_assessment_failed_state():

    assessment = (
        QualityAssessment(
            dimension="completeness",
            score=45.0,
            passed=False,
        )
    )

    result = (
        assessment.to_dict()
    )

    assert (
        result["passed"]
        is False
    )

    assert (
        result["score"]
        == 45.0
    )


def test_quality_assessment_zero_score():

    assessment = (
        QualityAssessment(
            dimension="validity",
            score=0.0,
            passed=False,
        )
    )

    assert (
        assessment.score
        == 0.0
    )


def test_quality_assessment_full_score():

    assessment = (
        QualityAssessment(
            dimension="completeness",
            score=100.0,
            passed=True,
        )
    )

    assert (
        assessment.score
        == 100.0
    )