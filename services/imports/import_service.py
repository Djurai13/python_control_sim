from typing import Any

from services.imports.import_registry import (
    ImportRegistry,
)


class ImportService:

    def __init__(
        self,
        registry: ImportRegistry,
    ) -> None:

        self.registry = registry

    def import_file(
        self,
        file_format: str,
        source: str,
    ) -> Any:

        normalized_format = (
            file_format.strip()
            .lower()
        )

        if not normalized_format:
            raise ValueError(
                "File format is required."
            )

        if not source.strip():
            raise ValueError(
                "Source is required."
            )

        importer = (
            self.registry.get_importer(
                normalized_format
            )
        )

        return (
            importer.import_data(
                source
            )
        )