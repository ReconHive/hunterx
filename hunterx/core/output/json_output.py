"""
JSON Output
"""

from __future__ import annotations

import json
from dataclasses import asdict

from hunterx.core.result import ScanResult
from hunterx.core.output.base import Output


class JSONOutput(Output):

    def write(
        self,
        result: ScanResult,
        filename: str,
    ) -> None:

        with open(
            filename,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                asdict(result),
                file,
                indent=4,
                ensure_ascii=False,
            )