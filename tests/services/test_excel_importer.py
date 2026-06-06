from pathlib import Path

from openpyxl import Workbook

from pytest import raises

from services.imports.excel_importer import (
    ExcelImporter,
)


def test_excel_importer_creation():

    importer = ExcelImporter()

    assert importer is not None


def test_reject_empty_source():

    importer = ExcelImporter()

    with raises(
        ValueError
    ):
        importer.import_data(
            ""
        )


def test_reject_missing_file():

    importer = ExcelImporter()

    with raises(
        ValueError
    ):
        importer.import_data(
            "missing.xlsx"
        )


def test_import_excel_file(
    tmp_path: Path,
):

    workbook = Workbook()

    worksheet = (
        workbook.active
    )

    worksheet.append(
        [
            "name",
            "age",
        ]
    )

    worksheet.append(
        [
            "Alice",
            30,
        ]
    )

    worksheet.append(
        [
            "Bob",
            25,
        ]
    )

    excel_file = (
        tmp_path
        / "sample.xlsx"
    )

    workbook.save(
        excel_file
    )

    importer = (
        ExcelImporter()
    )

    result = (
        importer.import_data(
            str(
                excel_file
            )
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
        == 25
    )


def test_import_empty_workbook(
    tmp_path: Path,
):

    workbook = Workbook()

    excel_file = (
        tmp_path
        / "empty.xlsx"
    )

    workbook.save(
        excel_file
    )

    importer = (
        ExcelImporter()
    )

    result = (
        importer.import_data(
            str(
                excel_file
            )
        )
    )

    assert (
        result["row_count"]
        == 0
    )

    assert (
        result["records"]
        == []
    )