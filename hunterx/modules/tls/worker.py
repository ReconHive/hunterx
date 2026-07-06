from __future__ import annotations

import socket
import ssl

from hunterx.modules.tls.parser import (
    CertificateParser,
)


class TLSWorker:

    def __init__(self) -> None:

        self.parser = CertificateParser()

    def scan(
        self,
        host: str,
        timeout: float,
    ) -> dict | None:

        context = ssl.create_default_context()

        try:

            with socket.create_connection(

                (
                    host,
                    443,
                ),

                timeout=timeout,

            ) as sock:

                with context.wrap_socket(

                    sock,

                    server_hostname=host,

                ) as tls:

                    cert = tls.getpeercert()

                    parsed = self.parser.parse(
                        cert,
                    )

                    return {

                        "enabled": True,

                        "version": tls.version(),

                        "cipher": tls.cipher()[0],

                        **parsed,

                    }

        except Exception:

            return None