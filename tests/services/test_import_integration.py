import json

from pathlib import Path

from openpyxl import Workbook

from pytest import raises

from services.imports.csv_importer import (
    CSVImporter,
)

from services.imports.excel_importer import (
    ExcelImporter,
)

from services.imports.geojson_importer import (
    GeoJSONImporter,
)

from services.imports.import_registry import (
    ImportRegistry,
)

from services.imports.import_service import (
    ImportService,
)


def build_registry() -> ImportRegistry:

    registry = ImportRegistry()

    registry.register_importer(
        "csv",
        CSVImporter(),
    )

    registry.register_importer(
        "xlsx",
        ExcelImporter(),
    )

    registry.register_importer(
        "geojson",
        GeoJSONImporter(),
    )

    return registry


def test_csv_import_integration(
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

    service = ImportService(
        registry=build_registry(),
    )

    result = service.import_file(
        "csv",
        str(csv_file),
    )

    assert (
        result["row_count"]
        == 2
    )

    assert (
        result["records"][0]["name"]
        == "Alice"
    )


def test_excel_import_integration(
    tmp_path: Path,
):

    workbook = Workbook()

    worksheet = (
        workbook.active
    )

    worksheet.append(
        ["name", "age"]
    )

    worksheet.append(
        ["Alice", 30]
    )

    worksheet.append(
        ["Bob", 25]
    )

    excel_file = (
        tmp_path
        / "sample.xlsx"
    )

    workbook.save(
        excel_file
    )

    service = ImportService(
        registry=build_registry(),
    )

    result = service.import_file(
        "xlsx",
        str(excel_file),
    )

    assert (
        result["row_count"]
        == 2
    )

    assert (
        result["records"][1]["name"]
        == "Bob"
    )


def test_geojson_import_integration(
    tmp_path: Path,
):

    geojson_file = (
        tmp_path
        / "sample.geojson"
    )

    geojson_file.write_text(
        json.dumps(
            {
                "type":
                "FeatureCollection",
                "features": [
                    {
                        "type":
                        "Feature",
                        "properties": {
                            "name":
                            "Location A",
                        },
                        "geometry": {
                            "type":
                            "Point",
                            "coordinates":
                            [1, 2],
                        },
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    service = ImportService(
        registry=build_registry(),
    )

    result = service.import_file(
        "geojson",
        str(geojson_file),
    )

    assert (
        result["feature_count"]
        == 1
    )

    assert (
        result["features"][0]
        ["properties"]
        ["name"]
        == "Location A"
    )


def test_reject_unknown_format():

    service = ImportService(
        registry=build_registry(),
    )

    with raises(
        ValueError
    ):
        service.import_file(
            "pdf",
            "sample.pdf",
        )


def test_registry_service_wiring(
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
        ),
        encoding="utf-8",
    )

    registry = (
        build_registry()
    )

    service = ImportService(
        registry=registry,
    )

    result = service.import_file(
        "csv",
        str(csv_file),
    )

    assert (
        result["row_count"]
        == 1
    )

    assert (
        registry.get_importer(
            "csv"
        ).__class__.__name__
        == "CSVImporter"
    )