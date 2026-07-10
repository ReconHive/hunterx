from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

from hunterx.core.context import ScanContext
from hunterx.modules.ports.common import DEFAULT_PORTS
from hunterx.modules.ports.worker import PortWorker


class PortScanner:

    def __init__(self) -> None:

        self.worker = PortWorker()

    def scan(
        self,
        context: ScanContext,
    ) -> tuple[
        list[int],
        dict[int, str],
        dict[int, str],
    ]:

        workers = (
            context.config.scanner.workers
        )

        timeout = (
            context.config.http.timeout
        )

        target_ports = (
            context.config.ports.ports
            or DEFAULT_PORTS
        )

        open_ports: list[int] = []

        services: dict[int, str] = {}

        banners: dict[int, str] = {}

        with ThreadPoolExecutor(
            max_workers=workers,
        ) as executor:

            futures = {

                executor.submit(
                    self.worker.scan,
                    context.target,
                    port,
                    timeout,
                ): port

                for port in target_ports

            }

            for future in as_completed(
                futures,
            ):

                result = future.result()

                if result is None:

                    continue

                port, service, banner = result

                open_ports.append(
                    port,
                )

                services[
                    port
                ] = service

                if banner:

                    banners[
                        port
                    ] = banner

        open_ports.sort()

        return (
            open_ports,
            services,
            banners,
        )