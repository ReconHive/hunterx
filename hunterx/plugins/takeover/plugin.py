from __future__ import annotations

from hunterx.cli.tables import takeover_findings

from hunterx.core.context import ScanContext
from hunterx.modules.takeover.scanner import TakeoverScanner
from hunterx.plugins.base import Plugin


class TakeoverPlugin(Plugin):

    name = "takeover"

    depends_on = ["subdomain"]

    def __init__(self) -> None:

        self.scanner = TakeoverScanner()

    def run(
        self,
        context: ScanContext,
    ) -> None:

        context.logger.info(
            "Checking for subdomain takeovers..."
        )

        findings = self.scanner.scan(
            context,
        )

        context.result.takeover.findings = findings

        if not findings:

            context.logger.success(
                "No takeover indicators found."
            )

        else:

            context.logger.error(
                f"{len(findings)} possible subdomain "
                "takeover(s) found!"
            )

            takeover_findings(
                "Possible Subdomain Takeovers",
                findings,
            )

        self.save_workspace(
            context,
            context.result.takeover,
        )