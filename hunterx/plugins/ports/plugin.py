from __future__ import annotations

import time

from hunterx.cli.tables import key_value
from hunterx.cli.tables import ports_table

from hunterx.core.context import ScanContext
from hunterx.modules.ports.parser import BannerParser
from hunterx.modules.ports.scanner import PortScanner
from hunterx.plugins.base import Plugin


class PortScannerPlugin(Plugin):

    name = "portscanner"

    def __init__(self) -> None:

        self.scanner = PortScanner()

        self.parser = BannerParser()

    def run(
        self,
        context: ScanContext,
    ) -> None:

        context.logger.info(
            "Starting port scan..."
        )

        start = time.perf_counter()

        ports, services, banners = self.scanner.scan(
            context,
        )

        elapsed = (
            time.perf_counter()
            - start
        )

        context.result.portscanner.open_ports = ports

        context.result.portscanner.services = services

        context.result.portscanner.banners = banners

        if not ports:

            context.logger.warning(
                "No open ports found."
            )

            self.save_workspace(
                context,
                context.result.portscanner,
            )

            return

        sensitive = [

            port

            for port in ports

            if services.get(port) in (
                "mysql",
                "postgres",
                "mssql",
                "oracle",
                "mongodb",
                "redis",
                "docker",
                "rdp",
                "vnc",
                "winrm",
                "smb",
                "telnet",
                "elasticsearch",
            )

        ]

        key_value(
            "Port Scan Summary",
            [
                (
                    "Target",
                    context.target,
                ),
                (
                    "Open Ports",
                    str(len(ports)),
                ),
                (
                    "Sensitive Services",
                    str(len(sensitive)),
                ),
                (
                    "Elapsed",
                    f"{elapsed:.2f}s",
                ),
            ],
        )

        if sensitive:

            context.logger.warning(
                f"{len(sensitive)} sensitive service(s) exposed "
                "- review exposure and authentication!"
            )

        versions: dict[int, str | None] = {}

        for port in ports:

            service = services[port]

            parsed = self.parser.parse(
                service,
                banners.get(port),
            )

            raw = banners.get(port)

            if parsed:

                versions[port] = parsed

            elif raw:

                versions[port] = (
                    raw[:60] + "..."
                    if len(raw) > 60
                    else raw
                )

            else:

                versions[port] = None

        ports_table(
            "Open Ports",
            ports,
            services,
            versions,
        )

        self.save_workspace(
            context,
            context.result.portscanner,
        )