"""
DNS Result Models
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class DNSResolveResult:
    """
    Result of resolving a hostname.
    """

    target: str

    address: str | None

    success: bool


@dataclass(slots=True)
class DNSRecordsResult:
    """
    Result of DNS record enumeration.
    """

    records: dict[str, list[str]] = field(default_factory=dict)