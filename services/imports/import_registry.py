from typing import Any


class ImportRegistry:

    def __init__(
        self,
    ) -> None:

        self._importers: dict[
            str,
            Any,
        ] = {}

    def register_importer(
        self,
        file_format: str,
        importer: Any,
    ) -> None:

        normalized_format = (
            file_format.strip()
            .lower()
        )

        if not normalized_format:
            raise ValueError(
                "File format is required."
            )

        if importer is None:
            raise ValueError(
                "Importer is required."
            )

        if (
            normalized_format
            in self._importers
        ):
            raise ValueError(
                f"Importer already "
                f"registered for "
                f"'{normalized_format}'."
            )

        self._importers[
            normalized_format
        ] = importer

    def get_importer(
        self,
        file_format: str,
    ) -> Any:

        normalized_format = (
            file_format.strip()
            .lower()
        )

        if not normalized_format:
            raise ValueError(
                "File format is required."
            )

        importer = (
            self._importers.get(
                normalized_format
            )
        )

        if importer is None:
            raise ValueError(
                f"No importer "
                f"registered for "
                f"'{normalized_format}'."
            )

        return importer

    def supported_formats(
        self,
    ) -> list[str]:

        return sorted(
            self._importers.keys()
        )