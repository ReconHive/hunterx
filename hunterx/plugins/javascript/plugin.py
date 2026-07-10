from __future__ import annotations

import time

from hunterx.cli.tables import key_value
from hunterx.cli.tables import preview
from hunterx.cli.tables import secrets as secrets_table

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

        start = time.perf_counter()

        result = self.scanner.scan(
            context,
        )

        elapsed = (
            time.perf_counter()
            - start
        )

        context.result.javascript = result

        if not result.files:

            context.logger.warning(
                "No JavaScript files found to analyze."
            )

            return

        key_value(
            "JavaScript Analysis Summary",
            [
                (
                    "Target",
                    context.target,
                ),
                (
                    "JS Files",
                    str(len(result.files)),
                ),
                (
                    "Endpoints",
                    str(len(result.endpoints)),
                ),
                (
                    "URLs",
                    str(len(result.urls)),
                ),
                (
                    "Domains",
                    str(len(result.domains)),
                ),
                (
                    "Secrets",
                    str(len(result.secrets)),
                ),
                (
                    "Elapsed",
                    f"{elapsed:.2f}s",
                ),
            ],
        )

        if result.secrets:

            context.logger.warning(
                f"{len(result.secrets)} possible secrets found "
                "- review before disclosure!"
            )

            secrets_table(
                "Possible Secrets",
                result.secrets,
            )

        if result.endpoints:

            preview(
                "Extracted Endpoints",
                "Endpoint",
                result.endpoints,
            )

        if result.urls:

            preview(
                "Extracted URLs",
                "URL",
                result.urls,
            )

        if result.domains:

            preview(
                "Extracted Domains",
                "Domain",
                result.domains,
            )

        workspace_path = (
            f".hunterx/{context.target}/javascript.json"
        )

        context.logger.info(
            f"Full results saved to {workspace_path}"
        )

        context.logger.info(
            f"View everything: cat {workspace_path}"
        )

        self.save_workspace(
            context,
            result,
        )