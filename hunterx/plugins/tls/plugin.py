from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.tls.scanner import TLSScanner
from hunterx.plugins.base import Plugin


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

        context.logger.success(
            f"TLS Version : {result['version']}"
        )

        context.logger.success(
            f"Cipher : {result['cipher']}"
        )

        context.logger.success(
            f"Issuer : {result['issuer']}"
        )

        context.logger.success(
            f"Subject : {result['subject']}"
        )

        context.logger.success(
            f"Expires : {result['expires']}"
        )

        context.logger.success(
            f"Days Remaining : {result['days_remaining']}"
        )

        if result["wildcard"]:

            context.logger.info(
                "Wildcard Certificate"
            )

        if result["self_signed"]:

            context.logger.warning(
                "Self Signed Certificate"
            )

        if result["expired"]:

            context.logger.error(
                "Certificate Expired"
            )

        if result["findings"]:

            context.logger.info(
                ""
            )

            context.logger.info(
                "TLS Findings"
            )

            for finding in result["findings"]:

                context.logger.warning(
                    f"- {finding}"
                )

        self.save_workspace(
            context,
            context.result.tls,
        )