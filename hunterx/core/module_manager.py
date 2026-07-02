"""
HunterX Module Manager
"""

from __future__ import annotations


class ModuleManager:

    def __init__(self) -> None:

        self.modules = []

    def register(self, module) -> None:

        self.modules.append(module)

    def execute(self, target: str) -> None:

        for module in self.modules:

            module(target)