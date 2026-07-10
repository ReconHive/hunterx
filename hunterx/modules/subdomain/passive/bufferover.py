from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.subdomain.source import PassiveSource


class BufferOver(PassiveSource):

    name = "BufferOver"

    def fetch(
        self,
        context: ScanContext,
    ) -> set[str]:

        url = (
            "https://dns.bufferover.run/dns"
            f"?q=.{context.target}"
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

        for key in (
            "FDNS_A",
            "RDNS",
        ):

            for record in data.get(
                key,
            ) or []:

                parts = record.split(
                    ",",
                )

                if len(parts) != 2:
                    continue

                host = parts[1].strip().lower()

                if not host.endswith(
                    context.target,
                ):
                    continue

                hosts.add(host)

        return hosts