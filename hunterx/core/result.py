"""
HunterX Scan Result Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from hunterx.modules.javascript.models import JavaScriptResult


@dataclass(slots=True)
class DNSResult:

    ip: str | None = None

    records: dict[str, list[str]] = field(
        default_factory=dict,
    )


@dataclass(slots=True)
class HTTPResult:

    status: int | None = None

    reason: str | None = None

    elapsed: float | None = None

    size: int | None = None

    server: str | None = None

    title: str | None = None

    url: str | None = None

    headers: dict[str, str] = field(
        default_factory=dict,
    )

    technologies: list[str] = field(
        default_factory=list,
    )

    security_headers: dict[str, str] = field(
        default_factory=dict,
    )

    cookies: list[dict] = field(
        default_factory=list,
    )

    cors: dict[str, str] = field(
        default_factory=dict,
    )


@dataclass(slots=True)
class SubdomainResult:

    hosts: list[str] = field(
        default_factory=list,
    )


@dataclass(slots=True)
class CrawlerResult:

    urls: list[str] = field(
        default_factory=list,
    )

    robots: list[str] = field(
        default_factory=list,
    )

    sitemap: list[str] = field(
        default_factory=list,
    )


@dataclass(slots=True)
class DirectoryResult:

    paths: list[str] = field(
        default_factory=list,
    )


@dataclass(slots=True)
class PortScannerResult:

    open_ports: list[int] = field(
        default_factory=list,
    )

    services: dict[int, str] = field(
        default_factory=dict,
    )

    banners: dict[int, str] = field(
        default_factory=dict,
    )


@dataclass(slots=True)
class TLSResult:

    enabled: bool = False

    version: str | None = None

    cipher: str | None = None

    issuer: str | None = None

    subject: str | None = None

    san: list[str] = field(
        default_factory=list,
    )

    expires: str | None = None

    days_remaining: int | None = None

    expired: bool = False

    self_signed: bool = False

    wildcard: bool = False

    serial: str | None = None

    signature_algorithm: str | None = None

    findings: list[str] = field(          # <-- این فیلد اضافه شد
        default_factory=list,
    )


@dataclass(slots=True)
class TakeoverResult:

    findings: list[dict] = field(
        default_factory=list,
    )


@dataclass(slots=True)
class ParamsResult:

    parameters: dict[str, list[str]] = field(
        default_factory=dict,
    )

    classified: dict[str, list[str]] = field(
        default_factory=dict,
    )

@dataclass(slots=True)
class ScanResult:

    dns: DNSResult = field(
        default_factory=DNSResult,
    )

    http: HTTPResult = field(
        default_factory=HTTPResult,
    )

    subdomains: SubdomainResult = field(
        default_factory=SubdomainResult,
    )

    crawler: CrawlerResult = field(
        default_factory=CrawlerResult,
    )

    directory: DirectoryResult = field(
        default_factory=DirectoryResult,
    )

    portscanner: PortScannerResult = field(
        default_factory=PortScannerResult,
    )

    tls: TLSResult = field(
        default_factory=TLSResult,
    )

    findings: list[str] = field(
        default_factory=list,
    )

    javascript: JavaScriptResult = field(
        default_factory=JavaScriptResult,
    )

    takeover: TakeoverResult = field(
        default_factory=TakeoverResult,
    )

    params: ParamsResult = field(
        default_factory=ParamsResult,
    )