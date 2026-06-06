from services.quality.quality_engine import (
    QualityEngine,
)

from services.quality.quality_service import (
    QualityService,
)


def test_quality_engine_creation():

    engine = (
        QualityEngine(
            QualityService()
        )
    )

    assert engine is not None


def test_dataset_assessment_success():

    engine = (
        QualityEngine(
            QualityService()
        )
    )

    records = [
        {
            "name": "John",
            "age": 30,
        },
        {
            "name": "Mary",
            "age": 25,
        },
    ]

    result = (
        engine.assess_dataset(
            records=records,
            total_records=2,
            valid_records=2,
        )
    )

    assert (
        result["passed"]
        is True
    )

    assert (
        result[
            "overall_score"
        ]
        == 100.0
    )


def test_dataset_assessment_failure():

    engine = (
        QualityEngine(
            QualityService()
        )
    )

    records = [
        {
            "name": "",
            "age": "",
        }
    ]

    result = (
        engine.assess_dataset(
            records=records,
            total_records=1,
            valid_records=0,
        )
    )

    assert (
        result["passed"]
        is False
    )


def test_overall_score_calculation():

    engine = (
        QualityEngine(
            QualityService()
        )
    )

    records = [
        {
            "name": "John",
            "age": "",
        }
    ]

    result = (
        engine.assess_dataset(
            records=records,
            total_records=10,
            valid_records=5,
        )
    )

    assert (
        result[
            "overall_score"
        ]
        == 50.0
    )


def test_quality_dimensions_exist():

    engine = (
        QualityEngine(
            QualityService()
        )
    )

    records = [
        {
            "name": "John",
            "age": 30,
        }
    ]

    result = (
        engine.assess_dataset(
            records=records,
            total_records=1,
            valid_records=1,
        )
    )

    assert (
        "completeness"
        in result
    )

    assert (
        "validity"
        in result
    )