from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.subdomain.source import PassiveSource


class AlienVault(PassiveSource):

    name = "AlienVault"

    def fetch(
        self,
        context: ScanContext,
    ) -> set[str]:

        url = (
            "https://otx.alienvault.com/api/v1/indicators/"
            f"domain/{context.target}/passive_dns"
        )

        try:

            response = context.http.get(
                url,
            )

        except Exception:

            return set()

        if response.status_code != 200:

            return set()

        try:

            data = response.json()

        except Exception:

            return set()

        hosts: set[str] = set()

        for entry in data.get(
            "passive_dns",
            [],
        ):

            hostname = entry.get(
                "hostname",
            )

            if not hostname:
                continue

            hostname = hostname.strip().lower()

            if not hostname.endswith(
                context.target,
            ):
                continue

            hosts.add(hostname)

        return hosts