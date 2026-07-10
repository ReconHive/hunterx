from __future__ import annotations

import re

from hunterx.core.context import ScanContext
from hunterx.modules.subdomain.source import PassiveSource


class RapidDNS(PassiveSource):

    name = "RapidDNS"

    def fetch(
        self,
        context: ScanContext,
    ) -> set[str]:

        url = (
            "https://rapiddns.io/subdomain/"
            f"{context.target}?full=1"
        )

        try:

            response = context.http.get(
                url,
            )

        except Exception:

            return set()

        if response.status_code != 200:

            return set()

        pattern = re.compile(
            r"[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
            r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*"
            rf"\.{re.escape(context.target)}"
        )

        hosts: set[str] = set()

        for match in pattern.findall(
            response.text,
        ):

            host = match.strip().lower()

            hosts.add(host)

        hosts.add(
            context.target,
        )

        hosts.discard(
            context.target,
        )

        return hosts