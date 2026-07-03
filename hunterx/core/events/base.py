from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime


@dataclass(slots=True)
class Event:

    timestamp: datetime = field(
        default_factory=datetime.now,
        init=False,
    )