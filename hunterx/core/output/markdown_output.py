"""
Markdown Output
"""

from __future__ import annotations

from hunterx.core.output.base import Output
from hunterx.core.result import ScanResult


class MarkdownOutput(Output):

    def write(
        self,
        result: ScanResult,
        filename: str,
    ) -> None:

        with open(
            filename,
            "w",
            encoding="utf-8",
        ) as file:

            file.write("# HunterX Report\n\n")

            file.write("## DNS\n")

            file.write(
                f"- IP: {result.dns.ip}\n\n"
            )

            file.write("## HTTP\n")

            file.write(
                f"- Status: {result.http.status}\n"
            )

            file.write(
                f"- Server: {result.http.server}\n"
            )

            file.write(
                f"- URL: {result.http.url}\n\n"
            )

            file.write(
                "## Subdomains\n"
            )

            for host in result.subdomains.hosts:

                file.write(
                    f"- {host}\n"
                )