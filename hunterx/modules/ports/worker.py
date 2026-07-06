from __future__ import annotations

import socket

from hunterx.modules.ports.banner import BannerGrabber
from hunterx.modules.ports.service import detect_service


class PortWorker:

    def __init__(self) -> None:

        self.banner = BannerGrabber()

    def scan(
        self,
        host: str,
        port: int,
        timeout: float,
    ) -> tuple[int, str, str | None] | None:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )

        sock.settimeout(
            timeout,
        )

        try:

            if sock.connect_ex(
                (host, port),
            ) != 0:

                return None

            service = detect_service(
                port,
            )

            banner = self.banner.grab(
                host,
                port,
                timeout,
            )

            return (
                port,
                service,
                banner,
            )

        except Exception:

            return None

        finally:

            sock.close()