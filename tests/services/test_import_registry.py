from pytest import raises

from services.imports.import_registry import (
    ImportRegistry,
)


def test_import_registry_creation():

    registry = ImportRegistry()

    assert registry is not None


def test_register_importer():

    registry = ImportRegistry()

    importer = object()

    registry.register_importer(
        "csv",
        importer,
    )

    assert (
        registry.get_importer(
            "csv"
        )
        is importer
    )


def test_reject_duplicate_importer():

    registry = ImportRegistry()

    importer = object()

    registry.register_importer(
        "csv",
        importer,
    )

    with raises(
        ValueError
    ):
        registry.register_importer(
            "csv",
            importer,
        )


def test_reject_empty_format():

    registry = ImportRegistry()

    with raises(
        ValueError
    ):
        registry.register_importer(
            "",
            object(),
        )


def test_reject_none_importer():

    registry = ImportRegistry()

    with raises(
        ValueError
    ):
        registry.register_importer(
            "csv",
            None,
        )


def test_get_importer():

    registry = ImportRegistry()

    importer = object()

    registry.register_importer(
        "csv",
        importer,
    )

    result = (
        registry.get_importer(
            "csv"
        )
    )

    assert (
        result
        is importer
    )


def test_reject_unknown_importer():

    registry = ImportRegistry()

    with raises(
        ValueError
    ):
        registry.get_importer(
            "csv"
        )


def test_supported_formats():

    registry = ImportRegistry()

    registry.register_importer(
        "csv",
        object(),
    )

    registry.register_importer(
        "xlsx",
        object(),
    )

    assert (
        registry.supported_formats()
        == [
            "csv",
            "xlsx",
        ]
    )


def test_format_normalization():

    registry = ImportRegistry()

    importer = object()

    registry.register_importer(
        " CSV ",
        importer,
    )

    result = (
        registry.get_importer(
            "csv"
        )
    )

    assert (
        result
        is importer
    )