from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.subdomain.source import PassiveSource


class CertSpotter(PassiveSource):

    name = "CertSpotter"

    def fetch(
        self,
        context: ScanContext,
    ) -> set[str]:

        url = (
            "https://api.certspotter.com/v1/issuances"
            f"?domain={context.target}"
            "&include_subdomains=true"
            "&expand=dns_names"
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

        for entry in data:

            for name in entry.get(
                "dns_names",
                [],
            ):

                name = name.strip().lower().replace(
                    "*.",
                    "",
                )

                if not name.endswith(
                    context.target,
                ):
                    continue

                hosts.add(name)

        return hosts