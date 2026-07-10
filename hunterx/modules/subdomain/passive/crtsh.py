from __future__ import annotations

import re

from hunterx.core.context import ScanContext
from hunterx.modules.subdomain.source import PassiveSource


class CRTSH(PassiveSource):

    name = "crt.sh"

    def fetch(
        self,
        context: ScanContext,
    ) -> set[str]:

        url = (
            "https://crt.sh/"
            f"?q=%25.{context.target}"
            "&output=json"
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

        for item in data:

            for field in (
                "common_name",
                "name_value",
            ):

                value = item.get(
                    field,
                )

                if not value:
                    continue

                for host in value.splitlines():

                    host = (
                        host.strip()
                        .lower()
                        .replace("*.", "")
                    )

                    if (
                        not host.endswith(
                            context.target,
                        )
                    ):
                        continue

                    if re.search(
                        r"\s",
                        host,
                    ):
                        continue

                    hosts.add(host)

        return hosts