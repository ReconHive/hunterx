from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from hunterx.core.result import ScanResult


class Plugin(ABC):

    name: str = "plugin"

    description: str = ""

    version: str = "0.1.0"

    @abstractmethod
    def run(
        self,
        target: str,
        result: ScanResult,
    ) -> None:
        ...