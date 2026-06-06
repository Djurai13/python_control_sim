from pathlib import Path

from pytest import raises

from services.imports.csv_importer import (
    CSVImporter,
)


def test_csv_importer_creation():

    importer = CSVImporter()

    assert importer is not None


def test_reject_empty_source():

    importer = CSVImporter()

    with raises(
        ValueError
    ):
        importer.import_data(
            ""
        )


def test_reject_missing_file():

    importer = CSVImporter()

    with raises(
        ValueError
    ):
        importer.import_data(
            "missing.csv"
        )


def test_import_csv_file(
    tmp_path: Path,
):

    csv_file = (
        tmp_path
        / "sample.csv"
    )

    csv_file.write_text(
        (
            "name,age\n"
            "Alice,30\n"
            "Bob,25\n"
        ),
        encoding="utf-8",
    )

    importer = CSVImporter()

    result = (
        importer.import_data(
            str(csv_file)
        )
    )

    assert (
        result["row_count"]
        == 2
    )

    assert (
        result["column_count"]
        == 2
    )

    assert (
        result["records"][0]
        ["name"]
        == "Alice"
    )

    assert (
        result["records"][1]
        ["age"]
        == "25"
    )


def test_import_empty_csv(
    tmp_path: Path,
):

    csv_file = (
        tmp_path
        / "empty.csv"
    )

    csv_file.write_text(
        "name,age\n",
        encoding="utf-8",
    )

    importer = CSVImporter()

    result = (
        importer.import_data(
            str(csv_file)
        )
    )

    assert (
        result["row_count"]
        == 0
    )

    assert (
        result["column_count"]
        == 0
    )

    assert (
        result["records"]
        == []
    )