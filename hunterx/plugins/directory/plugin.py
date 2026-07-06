from __future__ import annotations

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

        results = self.scanner.scan(
            context,
        )

        context.result.directory.paths = results

        if not results:

            context.logger.warning(
                "No interesting paths found."
            )

            return

        context.logger.success(
            f"Found {len(results)} paths"
        )

        for item in results:

            context.logger.success(item)

        self.save_workspace(
            context,
            context.result.directory,
        )