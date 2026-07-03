"""
HunterX Scan Context
"""

from __future__ import annotations

from dataclasses import dataclass

from hunterx.core.config import Config
from hunterx.core.logger import logger
from hunterx.core.result import ScanResult
from hunterx.core.http import HTTPPool


@dataclass(slots=True)
class ScanContext:
    """
    Shared context for every plugin.
    """

    target: str

    config: Config

    result: ScanResult

    logger = logger

    http: HTTPPool