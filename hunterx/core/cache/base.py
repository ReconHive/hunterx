from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any


class CacheBackend(ABC):

    @abstractmethod
    def get(
        self,
        key: str,
    ) -> Any | None:
        ...

    @abstractmethod
    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        ...

    @abstractmethod
    def delete(
        self,
        key: str,
    ) -> None:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...