from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.tls.worker import TLSWorker


class TLSScanner:

    def __init__(self) -> None:

        self.worker = TLSWorker()

    def scan(
        self,
        context: ScanContext,
    ) -> dict | None:

        return self.worker.scan(

            context.target,

            context.config.http.timeout,

        )