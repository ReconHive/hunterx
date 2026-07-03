"""
Base Output Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from hunterx.core.result import ScanResult


class Output(ABC):
    """
    Base class for all output writers.
    """

    @abstractmethod
    def write(
        self,
        result: ScanResult,
        filename: str,
    ) -> None:
        """
        Write scan results to a file.
        """
        raise NotImplementedError