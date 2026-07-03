from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Event:
    """
    Base event.
    """

    timestamp: datetime = datetime.now()