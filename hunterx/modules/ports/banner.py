from __future__ import annotations

import socket
import ssl


class BannerGrabber:

    def grab(
        self,
        host: str,
        port: int,
        timeout: float,
    ) -> str | None:

        try:

            sock = socket.create_connection(
                (host, port),
                timeout=timeout,
            )

            #
            # HTTPS
            #

            if port in (
                443,
                8443,
            ):

                context = ssl.create_default_context()

                sock = context.wrap_socket(
                    sock,
                    server_hostname=host,
                )

            #
            # HTTP
            #

            if port in (
                80,
                443,
                8080,
                8443,
            ):

                sock.sendall(
                    (
                        "HEAD / HTTP/1.0\r\n"
                        f"Host: {host}\r\n\r\n"
                    ).encode()
                )

            banner = sock.recv(
                1024,
            )

            sock.close()

            return banner.decode(
                errors="ignore",
            ).strip()

        except Exception:

            return None