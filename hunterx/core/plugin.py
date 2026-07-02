"""
HunterX Plugin API

Defines the base interface for every HunterX module.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Plugin(ABC):
    """
    Base class for every HunterX plugin.
    """

    name: str = "plugin"

    description: str = ""

    version: str = "0.1.0"

    author: str = "ReconHive"

    @abstractmethod
    async def execute(self, target: str) -> None:
        """
        Execute the plugin.
        """
        raise NotImplementedError