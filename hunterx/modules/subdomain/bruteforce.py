"""
Subdomain Bruteforce Engine
"""

from __future__ import annotations

import socket
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from hunterx.core.dns import DNSPool


class Bruteforce:

    def __init__(self, workers: int = 50) -> None:
        self.workers = workers
        self.pool = DNSPool()

    def _resolve(
        self,
        host: str,
    ) -> str | None:

        try:

            self.pool.resolve(host)

            return host

        except Exception:

            return None

    def scan(
        self,
        target: str,
        words: list[str],
    ) -> list[str]:

        found: list[str] = []

        hosts = [
            f"{word}.{target}"
            for word in words
        ]

        with ThreadPoolExecutor(
            max_workers=self.workers
        ) as executor:

            futures = [
                executor.submit(
                    self._resolve,
                    host,
                )
                for host in hosts
            ]

            for future in as_completed(futures):

                result = future.result()

                if result:

                    found.append(result)

        return sorted(found)