from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.tls.worker import TLSWorker
from hunterx.modules.tls.auditor import TLSAuditor


class TLSScanner:

    def __init__(self) -> None:

        self.worker = TLSWorker()

        self.auditor = TLSAuditor()

    def scan(
        self,
        context: ScanContext,
    ) -> dict | None:

        result = self.worker.scan(
            context.target,
            context.config.http.timeout,
        )

        if result is None:
            return None

        result["findings"] = self.auditor.audit(
            result,
        )

        return result