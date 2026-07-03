"""
Subdomain Bruteforce Engine
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

from hunterx.core.context import ScanContext


class Bruteforce:

    def _resolve(
        self,
        context: ScanContext,
        host: str,
    ) -> str | None:

        try:

            context.dns.resolve(host)

            return host

        except Exception:

            return None

    def scan(
        self,
        context: ScanContext,
        words: list[str],
    ) -> list[str]:

        found: list[str] = []

        hosts = [
            f"{word}.{context.target}"
            for word in words
        ]

        with ThreadPoolExecutor(
            max_workers=context.config.scanner.workers
        ) as executor:

            futures = [
                executor.submit(
                    self._resolve,
                    context,
                    host,
                )
                for host in hosts
            ]

            for future in as_completed(futures):

                result = future.result()

                if result:

                    found.append(result)

        return sorted(found)