from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from hunterx.core.context import ScanContext


class PassiveSource(ABC):

    name = "Unknown"

    @abstractmethod
    def fetch(
        self,
        context: ScanContext,
    ) -> set[str]:
        raise NotImplementedError