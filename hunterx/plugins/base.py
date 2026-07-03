from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from hunterx.core.result import ScanResult


class Plugin(ABC):
    """
    Base class for all HunterX plugins.
    """

    name: str = "plugin"

    @abstractmethod
    def run(
        self,
        target: str,
        result: ScanResult,
    ) -> None:
        """
        Execute plugin.
        """