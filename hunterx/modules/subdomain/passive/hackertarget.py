from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.subdomain.source import PassiveSource


class HackerTarget(PassiveSource):

    name = "HackerTarget"

    def fetch(
        self,
        context: ScanContext,
    ) -> set[str]:

        url = (
            "https://api.hackertarget.com/hostsearch/"
            f"?q={context.target}"
        )

        try:

            response = context.http.get(
                url,
            )

        except Exception:

            return set()

        if response.status_code != 200:

            return set()

        text = response.text

        if "error" in text.lower():
            return set()

        hosts: set[str] = set()

        for line in text.splitlines():

            parts = line.split(
                ",",
            )

            if not parts:
                continue

            host = parts[0].strip().lower()

            if not host.endswith(
                context.target,
            ):
                continue

            hosts.add(host)

        return hosts