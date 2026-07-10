from __future__ import annotations

from hunterx.core.context import ScanContext

from hunterx.modules.subdomain.passive import (
    AlienVault,
    BufferOver,
    CertSpotter,
    CRTSH,
    HackerTarget,
    RapidDNS,
    URLScan,
)


class PassiveManager:

    def __init__(self) -> None:

        self.sources = [
            CRTSH(),
            AlienVault(),
            BufferOver(),
            CertSpotter(),
            HackerTarget(),
            RapidDNS(),
            URLScan(),
        ]

    def scan(
        self,
        context: ScanContext,
    ) -> set[str]:

        hosts: set[str] = set()

        context.logger.info(
            "Running passive sources..."
        )

        for source in self.sources:

            try:

                result = source.fetch(
                    context,
                )

                hosts.update(result)

                context.logger.success(
                    f"{source.name:<15} {len(result)}"
                )

            except Exception as exc:

                context.logger.warning(
                    f"{source.name:<15} Failed ({exc})"
                )

        return hosts