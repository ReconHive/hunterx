"""
HunterX Scan Result Model
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field


@dataclass(slots=True)
class ScanResult:

    dns: dict = field(default_factory=dict)

    http: dict = field(default_factory=dict)

    subdomains: list[str] = field(
        default_factory=list
    )