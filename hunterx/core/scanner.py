"""
HunterX Scan Engine
"""

from __future__ import annotations

from hunterx.core.logger import logger
from hunterx.core.module_manager import ModuleManager
from hunterx.core.result import ScanResult

from hunterx.modules.dns.module import DNSModule
from hunterx.modules.http.module import HTTPModule
from hunterx.modules.subdomain.module import (
    SubdomainModule,
)


class ScanEngine:

    def __init__(
        self,
        result: ScanResult,
    ) -> None:

        self.result = result

        self.manager = ModuleManager()

        self.manager.register(
            DNSModule()
        )

        self.manager.register(
            HTTPModule()
        )

        self.manager.register(
            SubdomainModule()
        )

    def run(
        self,
        target: str,
    ) -> None:

        logger.info(
            "Starting scan pipeline..."
        )

        self.manager.execute(
            target,
            self.result,
        )

        logger.success(
            "Scan completed."
        )