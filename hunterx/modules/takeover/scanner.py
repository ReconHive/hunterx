from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

from hunterx.core.context import ScanContext
from hunterx.modules.takeover.worker import TakeoverWorker


class TakeoverScanner:

    def __init__(self) -> None:

        self.worker = TakeoverWorker()

    def scan(
        self,
        context: ScanContext,
    ) -> list[dict]:

        hosts = context.result.subdomains.hosts

        findings: list[dict] = []

        if not hosts:
            return findings

        workers = context.config.scanner.workers

        with ThreadPoolExecutor(
            max_workers=workers,
        ) as executor:

            futures = [

                executor.submit(
                    self.worker.check,
                    context,
                    host,
                )

                for host in hosts

            ]

            for future in as_completed(
                futures,
            ):

                result = future.result()

                if result is not None:

                    findings.append(
                        result,
                    )

        return findings