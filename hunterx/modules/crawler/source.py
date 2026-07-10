from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from hunterx.core.context import ScanContext


class CrawlerSource(ABC):

    name = "Unknown"

    field = "urls"

    @abstractmethod
    def fetch(
        self,
        context: ScanContext,
    ) -> list[str]:
        raise NotImplementedError