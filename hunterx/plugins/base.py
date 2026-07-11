from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from hunterx.core.context import ScanContext


class Plugin(ABC):

    name: str = "plugin"

    description: str = ""

    version: str = "0.1.0"

    depends_on: list[str] = []

    @abstractmethod
    def run(
        self,
        context: ScanContext,
    ) -> None:
        """
        Execute plugin.
        """

    def save_workspace(
        self,
        context: ScanContext,
        data: object,
    ) -> None:

        context.workspace.save(
            context.target,
            self.name,
            data,
        )