import csv
from pathlib import Path


class CSVImporter:

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
                "CSV file does not exist."
            )

        rows: list[dict] = []

        with open(
            file_path,
            mode="r",
            newline="",
            encoding="utf-8",
        ) as csv_file:

            reader = csv.DictReader(
                csv_file
            )

            for row in reader:
                rows.append(
                    dict(row)
                )

        column_count = 0

        if rows:
            column_count = len(
                rows[0]
            )

        return {
            "records": rows,
            "row_count": len(rows),
            "column_count": column_count,
        }