"""
HunterX Module Manager
"""

from __future__ import annotations

from hunterx.core.module import Module
from hunterx.core.result import ScanResult


class ModuleManager:

    def __init__(self) -> None:

        self.modules: list[Module] = []

    def register(
        self,
        module: Module,
    ) -> None:

        self.modules.append(module)

    def execute(
        self,
        target: str,
        result: ScanResult,
    ) -> None:

        for module in self.modules:

            module.run(
                target,
                result,
            )