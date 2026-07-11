from __future__ import annotations

from hunterx.cli.tables import key_value
from hunterx.cli.tables import params_findings

from hunterx.core.context import ScanContext
from hunterx.modules.params.common import HIGH_RISK_CATEGORIES
from hunterx.modules.params.scanner import ParamsScanner
from hunterx.plugins.base import Plugin


class ParamsPlugin(Plugin):

    name = "params"

    depends_on = ["crawler"]

    def __init__(self) -> None:

        self.scanner = ParamsScanner()

    def run(
        self,
        context: ScanContext,
    ) -> None:

        context.logger.info(
            "Extracting parameters..."
        )

        result = self.scanner.scan(
            context,
        )

        context.result.params.parameters = result["parameters"]

        context.result.params.classified = result["classified"]

        if not result["parameters"]:

            context.logger.warning(
                "No parameters found."
            )

            self.save_workspace(
                context,
                context.result.params,
            )

            return

        classified = result["classified"]

        summary_rows = sorted(
            (
                (category, str(len(names)))
                for category, names in classified.items()
            ),
            key=lambda row: -int(row[1]),
        )

        key_value(
            "Parameter Extraction Summary",
            [
                (
                    "Target",
                    context.target,
                ),
                (
                    "Unique Parameters",
                    str(len(result["parameters"])),
                ),
                *summary_rows,
            ],
        )

        high_risk_found = {
            category: names
            for category, names in classified.items()
            if category in HIGH_RISK_CATEGORIES
            and names
        }

        if high_risk_found:

            context.logger.warning(
                f"{sum(len(v) for v in high_risk_found.values())} "
                "high-risk parameter(s) found - review for IDOR, "
                "SSRF, LFI, redirect, or injection potential"
            )

            for category, names in high_risk_found.items():

                params_findings(
                    category,
                    names,
                    result["parameters"],
                )

        self.save_workspace(
            context,
            context.result.params,
        )