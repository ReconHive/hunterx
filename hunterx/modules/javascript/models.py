from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field


@dataclass(slots=True)
class JavaScriptFile:

    url: str

    content: str


@dataclass(slots=True)
class JavaScriptResult:

    files: list[str] = field(
        default_factory=list,
    )

    endpoints: list[str] = field(
        default_factory=list,
    )

    urls: list[str] = field(
        default_factory=list,
    )

    domains: list[str] = field(
        default_factory=list,
    )

    secrets: list[str] = field(
        default_factory=list,
    )