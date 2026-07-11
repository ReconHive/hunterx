from __future__ import annotations

import re

from urllib.parse import parse_qs
from urllib.parse import urlparse


_DIRECTORY_ROW_RE = re.compile(
    r"^\[\d{3}\]\s+(\S+)"
)


def extract_directory_url(
    row: str,
) -> str | None:
    """
    DirectoryScanner rows look like "[200] https://... -> loc".
    Pull the bare URL back out.
    """

    match = _DIRECTORY_ROW_RE.match(
        row,
    )

    if match:

        return match.group(1)

    return None


def extract_params(
    urls: list[str],
) -> dict[str, list[str]]:
    """
    Returns {param_name: [example_url, ...]} - up to 5 example
    URLs kept per parameter name, deduplicated.
    """

    params: dict[str, list[str]] = {}

    for url in urls:

        parsed = urlparse(
            url,
        )

        if not parsed.query:
            continue

        query = parse_qs(
            parsed.query,
            keep_blank_values=True,
        )

        for name in query:

            examples = params.setdefault(
                name,
                [],
            )

            if (
                url not in examples
                and len(examples) < 5
            ):

                examples.append(
                    url,
                )

    return params