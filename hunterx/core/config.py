"""
HunterX Configuration

Central configuration object for the framework.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Settings:
    """
    Global HunterX settings.
    """

    timeout: int = 10

    retries: int = 2

    threads: int = 10

    verify_ssl: bool = True

    user_agent: str = (
        "HunterX/0.1.0"
    )