from __future__ import annotations

import time

from hunterx.cli.tables import directory_results
from hunterx.cli.tables import key_value

from hunterx.core.context import ScanContext
from hunterx.modules.directory.scanner import DirectoryScanner
from hunterx.plugins.base import Plugin


class DirectoryPlugin(Plugin):

    name = "directory"

    def __init__(self) -> None:

        self.scanner = DirectoryScanner()

    def run(
        self,
        context: ScanContext,
    ) -> None:

        context.logger.info(
            "Starting directory scan..."
        )

        start = time.perf_counter()

        results = self.scanner.scan(
            context,
        )

        elapsed = (
            time.perf_counter()
            - start
        )

        context.result.directory.paths = results

        counts = {
            "2xx": 0,
            "3xx": 0,
            "4xx": 0,
            "other": 0,
        }

        for row in results:

            if row.startswith("[2"):
                counts["2xx"] += 1

            elif row.startswith("[3"):
                counts["3xx"] += 1

            elif row.startswith("[4"):
                counts["4xx"] += 1

            else:
                counts["other"] += 1

        key_value(
            "Directory Scan Summary",
            [
                (
                    "Target",
                    context.target,
                ),
                (
                    "Found",
                    str(len(results)),
                ),
                (
                    "2xx",
                    str(counts["2xx"]),
                ),
                (
                    "3xx",
                    str(counts["3xx"]),
                ),
                (
                    "4xx",
                    str(counts["4xx"]),
                ),
                (
                    "Elapsed",
                    f"{elapsed:.2f}s",
                ),
            ],
        )

        if not results:

            context.logger.warning(
                "No interesting paths found."
            )

            return

        directory_results(
            "Discovered Paths",
            results,
        )

        self.save_workspace(
            context,
            context.result.directory,
        )