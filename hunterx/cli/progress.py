from __future__ import annotations

from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)

progress = Progress(
    SpinnerColumn(),
    TextColumn("[plugin]{task.description}"),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    transient=False,
)