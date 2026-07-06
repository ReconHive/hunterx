from __future__ import annotations

import re


class BannerParser:

    def parse(
        self,
        service: str,
        banner: str | None,
    ) -> str | None:

        if not banner:

            return None

        if service == "ssh":

            m = re.search(
                r"OpenSSH[_\- ]([^\s]+)",
                banner,
                re.I,
            )

            if m:

                return f"OpenSSH {m.group(1)}"

        elif service in (
            "http",
            "https",
        ):

            m = re.search(
                r"Server:\s*(.+)",
                banner,
                re.I,
            )

            if m:

                return m.group(1).strip()

        return None