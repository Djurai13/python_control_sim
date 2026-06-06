from services.quality.quality_service import (
    QualityService,
)


def test_quality_service_creation():

    service = (
        QualityService()
    )

    assert service is not None


def test_completeness_full_score():

    service = (
        QualityService()
    )

    records = [
        {
            "name": "John",
            "age": 30,
        }
    ]

    result = (
        service.assess_completeness(
            records
        )
    )

    assert (
        result.score
        == 100.0
    )

    assert (
        result.passed
        is True
    )


def test_completeness_partial_score():

    service = (
        QualityService()
    )

    records = [
        {
            "name": "John",
            "age": "",
        }
    ]

    result = (
        service.assess_completeness(
            records
        )
    )

    assert (
        result.score
        == 50.0
    )

    assert (
        result.passed
        is False
    )


def test_completeness_empty_dataset():

    service = (
        QualityService()
    )

    result = (
        service.assess_completeness(
            []
        )
    )

    assert (
        result.score
        == 0.0
    )

    assert (
        result.passed
        is False
    )


def test_validity_full_score():

    service = (
        QualityService()
    )

    result = (
        service.assess_validity(
            total_records=10,
            valid_records=10,
        )
    )

    assert (
        result.score
        == 100.0
    )

    assert (
        result.passed
        is True
    )


def test_validity_partial_score():

    service = (
        QualityService()
    )

    result = (
        service.assess_validity(
            total_records=10,
            valid_records=5,
        )
    )

    assert (
        result.score
        == 50.0
    )

    assert (
        result.passed
        is False
    )


def test_validity_empty_dataset():

    service = (
        QualityService()
    )

    result = (
        service.assess_validity(
            total_records=0,
            valid_records=0,
        )
    )

    assert (
        result.score
        == 0.0
    )

    assert (
        result.passed
        is False
    )