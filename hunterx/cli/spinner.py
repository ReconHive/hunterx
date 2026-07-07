from __future__ import annotations

from contextlib import contextmanager

from rich.console import Console
from rich.status import Status

console = Console()


@contextmanager
def spinner(text: str):

    with console.status(
        text,
        spinner="dots",
    ) as status:

        yield status