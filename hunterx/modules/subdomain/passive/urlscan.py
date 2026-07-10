from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.subdomain.source import PassiveSource


class URLScan(PassiveSource):

    name = "URLScan"

    def fetch(
        self,
        context: ScanContext,
    ) -> set[str]:

        url = (
            "https://urlscan.io/api/v1/search/"
            f"?q=domain:{context.target}"
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
            "results",
            [],
        ):

            page = entry.get(
                "page",
                {},
            )

            domain = page.get(
                "domain",
            )

            if not domain:
                continue

            domain = domain.strip().lower()

            if not domain.endswith(
                context.target,
            ):
                continue

            hosts.add(domain)

        return hosts