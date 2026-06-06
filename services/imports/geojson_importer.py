import json

from pathlib import Path


class GeoJSONImporter:

    def import_data(
        self,
        source: str,
    ) -> dict:

        if not source.strip():
            raise ValueError(
                "Source is required."
            )

        file_path = Path(
            source
        )

        if not file_path.exists():
            raise ValueError(
                "GeoJSON file does not exist."
            )

        with open(
            file_path,
            mode="r",
            encoding="utf-8",
        ) as geojson_file:

            data = json.load(
                geojson_file
            )

        if (
            data.get("type")
            != "FeatureCollection"
        ):
            raise ValueError(
                "Invalid GeoJSON FeatureCollection."
            )

        features = data.get(
            "features",
            []
        )

        return {
            "features": features,
            "feature_count": len(
                features
            ),
        }