from __future__ import annotations

from typing import Any

from hunterx.core.cache.memory import MemoryCache


class CacheManager:

    def __init__(self) -> None:

        self.backend = MemoryCache()

    def get(
        self,
        key: str,
    ) -> Any | None:

        return self.backend.get(key)

    def set(
        self,
        key: str,
        value: Any,
    ) -> None:

        self.backend.set(
            key,
            value,
        )

    def delete(
        self,
        key: str,
    ) -> None:

        self.backend.delete(key)

    def clear(self) -> None:

        self.backend.clear()