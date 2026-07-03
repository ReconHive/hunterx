from __future__ import annotations

from dataclasses import dataclass

from hunterx.core.config import Config
from hunterx.core.container import ServiceContainer
from hunterx.core.dns import DNSPool
from hunterx.core.events.bus import EventBus
from hunterx.core.http import HTTPPool
from hunterx.core.logger import logger
from hunterx.core.result import ScanResult
from hunterx.core.metrics.manager import MetricsManager


@dataclass(slots=True)
class ScanContext:
    """
    Shared context for every plugin.
    """

    target: str

    config: Config

    result: ScanResult

    container: ServiceContainer

    http: HTTPPool

    dns: DNSPool

    events: EventBus

    metrics: MetricsManager

    logger = logger