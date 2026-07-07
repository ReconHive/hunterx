from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.javascript.scanner import JavaScriptScanner
from hunterx.plugins.base import Plugin


class JavaScriptPlugin(Plugin):

    name = "javascript"

    def __init__(self) -> None:

        self.scanner = JavaScriptScanner()

    def run(
        self,
        context: ScanContext,
    ) -> None:

        context.logger.info(
            "Analyzing JavaScript..."
        )

        result = self.scanner.scan(
            context,
        )

        context.result.javascript = result

        self.save_workspace(
            context,
            result,
        )