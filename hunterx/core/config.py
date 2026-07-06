"""
HunterX Configuration
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class DNSConfig:

    timeout: float = 2.0

    lifetime: float = 2.0

    nameservers: list[str] = field(
        default_factory=lambda: [
            "1.1.1.1",
            "8.8.8.8",
            "9.9.9.9",
        ]
    )


@dataclass(slots=True)
class ScannerConfig:

    workers: int = 50

    retries: int = 2


@dataclass(slots=True)
class HTTPConfig:

    timeout: float = 10.0

    follow_redirects: bool = True

    retries: int = 3

    backoff: float = 0.5


@dataclass(slots=True)
class CrawlerConfig:

    depth: int = 2

    max_pages: int = 100

    follow_redirects: bool = True

    internal_only: bool = True


@dataclass(slots=True)
class DirectoryConfig:

    follow_redirects: bool = False

    wordlist: str | None = None

    threads: int | None = None

    extensions: list[str] = field(
        default_factory=list,
    )

    include_status: tuple[int, ...] = (
        200,
        204,
        301,
        302,
        307,
        308,
        401,
        403,
    )

    exclude_status: tuple[int, ...] = ()


@dataclass(slots=True)
class Config:

    dns: DNSConfig = field(
        default_factory=DNSConfig
    )

    scanner: ScannerConfig = field(
        default_factory=ScannerConfig
    )

    http: HTTPConfig = field(
        default_factory=HTTPConfig
    )

    crawler: CrawlerConfig = field(
        default_factory=CrawlerConfig
    )

    directory: DirectoryConfig = field(
        default_factory=DirectoryConfig,
    )