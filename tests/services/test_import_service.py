from unittest.mock import Mock

from pytest import raises

from services.imports.import_registry import (
    ImportRegistry,
)

from services.imports.import_service import (
    ImportService,
)


def test_import_service_creation():

    registry = ImportRegistry()

    service = ImportService(
        registry=registry,
    )

    assert service is not None


def test_reject_empty_format():

    registry = ImportRegistry()

    service = ImportService(
        registry=registry,
    )

    with raises(
        ValueError
    ):
        service.import_file(
            "",
            "file.csv",
        )


def test_reject_empty_source():

    registry = ImportRegistry()

    service = ImportService(
        registry=registry,
    )

    with raises(
        ValueError
    ):
        service.import_file(
            "csv",
            "",
        )


def test_reject_unknown_format():

    registry = ImportRegistry()

    service = ImportService(
        registry=registry,
    )

    with raises(
        ValueError
    ):
        service.import_file(
            "csv",
            "file.csv",
        )


def test_import_file():

    registry = ImportRegistry()

    importer = Mock()

    importer.import_data.return_value = {
        "records": 10,
    }

    registry.register_importer(
        "csv",
        importer,
    )

    service = ImportService(
        registry=registry,
    )

    result = (
        service.import_file(
            "csv",
            "file.csv",
        )
    )

    assert result == {
        "records": 10,
    }

    importer.import_data.assert_called_once_with(
        "file.csv"
    )


def test_format_normalization():

    registry = ImportRegistry()

    importer = Mock()

    importer.import_data.return_value = {
        "records": 5,
    }

    registry.register_importer(
        "csv",
        importer,
    )

    service = ImportService(
        registry=registry,
    )

    result = (
        service.import_file(
            " CSV ",
            "file.csv",
        )
    )

    assert result == {
        "records": 5,
    }


def test_multiple_importers():

    registry = ImportRegistry()

    csv_importer = Mock()

    excel_importer = Mock()

    csv_importer.import_data.return_value = (
        "csv_result"
    )

    excel_importer.import_data.return_value = (
        "excel_result"
    )

    registry.register_importer(
        "csv",
        csv_importer,
    )

    registry.register_importer(
        "xlsx",
        excel_importer,
    )

    service = ImportService(
        registry=registry,
    )

    csv_result = (
        service.import_file(
            "csv",
            "data.csv",
        )
    )

    excel_result = (
        service.import_file(
            "xlsx",
            "data.xlsx",
        )
    )

    assert (
        csv_result
        == "csv_result"
    )

    assert (
        excel_result
        == "excel_result"
    )