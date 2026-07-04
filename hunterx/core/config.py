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


@dataclass(slots=True)
class CrawlerConfig:

    depth: int = 2

    max_pages: int = 100

    follow_redirects: bool = True

    internal_only: bool = True

@dataclass(slots=True)
class DirectoryConfig:

    threads: int = 30

    timeout: float = 5.0

    extensions: list[str] = field(
        default_factory=lambda: [
            "",
            ".php",
            ".asp",
            ".aspx",
            ".jsp",
            ".html",
        ]
    )

    status_codes: set[int] = field(
        default_factory=lambda: {
            200,
            204,
            301,
            302,
            307,
            401,
            403,
        }
    )

    max_words: int = 500






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