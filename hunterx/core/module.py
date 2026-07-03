"""
HunterX Module Interface
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from hunterx.core.result import ScanResult


class Module(ABC):

    name: str = ""

    @abstractmethod
    def run(
        self,
        target: str,
        result: ScanResult,
    ) -> None:
        ...