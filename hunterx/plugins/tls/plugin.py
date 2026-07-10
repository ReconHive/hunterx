from __future__ import annotations

from hunterx.cli.tables import findings as findings_table
from hunterx.cli.tables import key_value

from hunterx.core.context import ScanContext
from hunterx.modules.tls.scanner import TLSScanner
from hunterx.plugins.base import Plugin


def _days_style(
    days: int | None,
    expired: bool,
) -> str:

    if expired or (
        days is not None
        and days < 0
    ):
        return "error"

    if (
        days is not None
        and days < 30
    ):
        return "warning"

    return "success"


class TLSPlugin(Plugin):

    name = "tls"

    def __init__(self) -> None:

        self.scanner = TLSScanner()

    def run(
        self,
        context: ScanContext,
    ) -> None:

        context.logger.info(
            "Checking TLS..."
        )

        result = self.scanner.scan(
            context,
        )

        if result is None:

            context.logger.warning(
                "TLS not available. (On HTTP)"
            )

            return

        context.result.tls.enabled = True

        context.result.tls.version = result["version"]

        context.result.tls.cipher = result["cipher"]

        context.result.tls.issuer = result["issuer"]

        context.result.tls.subject = result["subject"]

        context.result.tls.san = result["san"]

        context.result.tls.expires = result["expires"]

        context.result.tls.days_remaining = result["days_remaining"]

        context.result.tls.expired = result["expired"]

        context.result.tls.self_signed = result["self_signed"]

        context.result.tls.wildcard = result["wildcard"]

        context.result.tls.serial = result["serial"]

        context.result.tls.signature_algorithm = result["signature_algorithm"]

        context.result.tls.findings = result["findings"]

        days_style = _days_style(
            result["days_remaining"],
            result["expired"],
        )

        san_display = (
            ", ".join(result["san"][:5])
            + (
                f" (+{len(result['san']) - 5} more)"
                if len(result["san"]) > 5
                else ""
            )
            if result["san"]
            else "-"
        )

        key_value(
            "TLS Certificate",
            [
                (
                    "Target",
                    context.target,
                ),
                (
                    "Version",
                    result["version"] or "-",
                ),
                (
                    "Cipher",
                    result["cipher"] or "-",
                ),
                (
                    "Issuer",
                    result["issuer"] or "-",
                ),
                (
                    "Subject",
                    result["subject"] or "-",
                ),
                (
                    "SAN",
                    san_display,
                ),
                (
                    "Expires",
                    result["expires"] or "-",
                ),
                (
                    "Days Remaining",
                    f"[{days_style}]{result['days_remaining']}[/{days_style}]"
                    if result["days_remaining"] is not None
                    else "-",
                ),
                (
                    "Serial",
                    result["serial"] or "-",
                ),
                (
                    "Signature Algorithm",
                    result["signature_algorithm"] or "-",
                ),
            ],
        )

        if result["findings"]:

            findings_table(
                "TLS Findings",
                result["findings"],
            )

        self.save_workspace(
            context,
            context.result.tls,
        )