"""
Output Manager
"""

from __future__ import annotations

from hunterx.core.output.json_output import JSONOutput
from hunterx.core.output.markdown_output import MarkdownOutput


class OutputManager:

    def __init__(self):

        self.outputs = {

            "json": JSONOutput(),

            "md": MarkdownOutput(),
        }

    def write(

        self,

        fmt: str,

        result,

        filename: str,

    ):

        writer = self.outputs.get(fmt)

        if writer:

            writer.write(

                result,

                filename,

            )