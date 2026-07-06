from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.ports.scanner import PortScanner
from hunterx.plugins.base import Plugin


class PortScannerPlugin(Plugin):

    name = "portscanner"

    def __init__(self) -> None:

        self.scanner = PortScanner()

    def run(
        self,
        context: ScanContext,
    ) -> None:

        context.logger.info(
            "Starting port scan..."
        )

        ports, services, banners = self.scanner.scan(
            context,
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

        context.logger.success(
            f"Found {len(ports)} open ports"
        )

        for port in ports:

            context.logger.success(
                f"{port}/tcp ({services[port]})"
            )

            banner = banners.get(
                port,
            )

            if banner:

                context.logger.info(
                    f"Banner: {banner}"
                )

        self.save_workspace(
            context,
            context.result.portscanner,
        )