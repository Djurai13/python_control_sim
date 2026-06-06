import json

from pathlib import Path

from pytest import raises

from services.imports.geojson_importer import (
    GeoJSONImporter,
)


def test_geojson_importer_creation():

    importer = (
        GeoJSONImporter()
    )

    assert importer is not None


def test_reject_empty_source():

    importer = (
        GeoJSONImporter()
    )

    with raises(
        ValueError
    ):
        importer.import_data(
            ""
        )


def test_reject_missing_file():

    importer = (
        GeoJSONImporter()
    )

    with raises(
        ValueError
    ):
        importer.import_data(
            "missing.geojson"
        )


def test_reject_invalid_geojson(
    tmp_path: Path,
):

    geojson_file = (
        tmp_path
        / "invalid.geojson"
    )

    geojson_file.write_text(
        json.dumps(
            {
                "type": "Point",
            }
        ),
        encoding="utf-8",
    )

    importer = (
        GeoJSONImporter()
    )

    with raises(
        ValueError
    ):
        importer.import_data(
            str(
                geojson_file
            )
        )


def test_import_geojson_file(
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
                    },
                    {
                        "type":
                        "Feature",
                        "properties": {
                            "name":
                            "Location B",
                        },
                        "geometry": {
                            "type":
                            "Point",
                            "coordinates":
                            [3, 4],
                        },
                    },
                ],
            }
        ),
        encoding="utf-8",
    )

    importer = (
        GeoJSONImporter()
    )

    result = (
        importer.import_data(
            str(
                geojson_file
            )
        )
    )

    assert (
        result[
            "feature_count"
        ]
        == 2
    )

    assert (
        result[
            "features"
        ][0][
            "properties"
        ]["name"]
        == "Location A"
    )


def test_import_empty_feature_collection(
    tmp_path: Path,
):

    geojson_file = (
        tmp_path
        / "empty.geojson"
    )

    geojson_file.write_text(
        json.dumps(
            {
                "type":
                "FeatureCollection",
                "features": [],
            }
        ),
        encoding="utf-8",
    )

    importer = (
        GeoJSONImporter()
    )

    result = (
        importer.import_data(
            str(
                geojson_file
            )
        )
    )

    assert (
        result[
            "feature_count"
        ]
        == 0
    )

    assert (
        result[
            "features"
        ]
        == []
    )