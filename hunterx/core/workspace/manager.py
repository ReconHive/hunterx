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

        WorkspaceStorage(
            target,
        ).save(
            name,
            data,
        )

    def load(
        self,
        target: str,
        name: str,
    ) -> Any | None:

        return WorkspaceStorage(
            target,
        ).load(
            name,
        )

    def exists(
        self,
        target: str,
        name: str,
    ) -> bool:

        return WorkspaceStorage(
            target,
        ).exists(
            name,
        )

    def delete(
        self,
        target: str,
        name: str,
    ) -> None:

        WorkspaceStorage(
            target,
        ).delete(
            name,
        )

    def list(
        self,
        target: str,
    ) -> list[str]:

        storage = WorkspaceStorage(
            target,
        )

        return [
            file.stem
            for file in storage.path.glob(
                "*.json",
            )
        ]

    def clear(
        self,
        target: str,
    ) -> None:

        WorkspaceStorage(
            target,
        ).clear()