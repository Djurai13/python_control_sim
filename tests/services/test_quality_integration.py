from services.quality.quality_engine import (
    QualityEngine,
)

from services.quality.quality_service import (
    QualityService,
)


def build_engine():

    return QualityEngine(
        QualityService()
    )


def test_quality_pipeline_success():

    engine = build_engine()

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

    assert result["passed"] is True

    assert (
        result["overall_score"]
        == 100.0
    )


def test_quality_pipeline_failure():

    engine = build_engine()

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

    assert result["passed"] is False


def test_completeness_dimension_present():

    engine = build_engine()

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
        result["completeness"]
        ["dimension"]
        == "completeness"
    )


def test_validity_dimension_present():

    engine = build_engine()

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
        result["validity"]
        ["dimension"]
        == "validity"
    )


def test_partial_quality_score():

    engine = build_engine()

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
        result["overall_score"]
        == 50.0
    )