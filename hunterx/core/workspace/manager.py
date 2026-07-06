from __future__ import annotations

from typing import Any

from hunterx.core.workspace.storage import WorkspaceStorage


class WorkspaceManager:

    def save(
        self,
        target: str,
        name: str,
        data: Any,
    ) -> None:

        storage = WorkspaceStorage(target)

        storage.save(
            name,
            data,
        )

    def load(
        self,
        target: str,
        name: str,
    ) -> Any | None:

        storage = WorkspaceStorage(target)

        return storage.load(
            name,
        )

    def exists(
        self,
        target: str,
        name: str,
    ) -> bool:

        storage = WorkspaceStorage(target)

        return storage.exists(
            name,
        )

    def delete(
        self,
        target: str,
        name: str,
    ) -> None:

        storage = WorkspaceStorage(target)

        storage.delete(
            name,
        )

    def list(
        self,
        target: str,
    ) -> list[str]:

        storage = WorkspaceStorage(target)

        return [
            file.stem
            for file in storage.path.glob("*.json")
        ]

    def clear(
        self,
        target: str,
    ) -> None:

        storage = WorkspaceStorage(target)

        storage.clear()