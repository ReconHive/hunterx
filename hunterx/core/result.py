"""
HunterX Scan Result Model
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class DNSResult:

    ip: str | None = None

    records: dict[str, list[str]] = field(
        default_factory=dict
    )


@dataclass(slots=True)
class HTTPResult:

    status: int | None = None

    server: str | None = None

    title: str | None = None

    url: str | None = None

    headers: dict[str, str] = field(
        default_factory=dict
    )

    technologies: list[str] = field(
        default_factory=list
    )

    security_headers: dict[str, str] = field(
        default_factory=dict
    )

    cookies: list[dict] = field(
        default_factory=list
    )

    cors: dict[str, str] = field(
        default_factory=dict
    )


@dataclass(slots=True)
class SubdomainResult:

    hosts: list[str] = field(
        default_factory=list
    )


@dataclass(slots=True)
class ScanResult:

    dns: DNSResult = field(
        default_factory=DNSResult
    )

    http: HTTPResult = field(
        default_factory=HTTPResult
    )

    subdomains: SubdomainResult = field(
        default_factory=SubdomainResult
    )