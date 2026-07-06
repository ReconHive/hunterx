from __future__ import annotations

import json
import shutil

from dataclasses import asdict
from dataclasses import is_dataclass

from pathlib import Path

from typing import Any


class WorkspaceStorage:

    ROOT = Path(".hunterx")

    def __init__(
        self,
        target: str,
    ) -> None:

        self.path = (
            self.ROOT /
            target
        )

        self.path.mkdir(
            parents=True,
            exist_ok=True,
        )

    def _serialize(
        self,
        data: Any,
    ) -> Any:

        #
        # Pydantic v2
        #

        if hasattr(
            data,
            "model_dump",
        ):

            return data.model_dump()

        #
        # Pydantic v1
        #

        if hasattr(
            data,
            "dict",
        ):

            return data.dict()

        #
        # Dataclass
        #

        if is_dataclass(
            data,
        ):

            return asdict(
                data,
            )

        #
        # Native types
        #

        return data

    def save(
        self,
        name: str,
        data: Any,
    ) -> None:

        file = self.path / f"{name}.json"

        file.write_text(
            json.dumps(
                self._serialize(
                    data,
                ),
                indent=4,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

    def load(
        self,
        name: str,
    ) -> Any | None:

        file = self.path / f"{name}.json"

        if not file.exists():

            return None

        return json.loads(
            file.read_text(
                encoding="utf-8",
            )
        )

    def exists(
        self,
        name: str,
    ) -> bool:

        return (
            self.path /
            f"{name}.json"
        ).exists()

    def delete(
        self,
        name: str,
    ) -> None:

        file = self.path / f"{name}.json"

        if file.exists():

            file.unlink()

    def clear(
        self,
    ) -> None:

        if self.path.exists():

            shutil.rmtree(
                self.path,
            )

        self.path.mkdir(
            parents=True,
            exist_ok=True,
        )