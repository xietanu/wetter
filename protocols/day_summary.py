"""A summary of the weather for a day."""
from typing import Protocol
import datetime

import protocols


class DaySummary(Protocol):
    """A summary of the weather for a day."""

    date: datetime.date
    description: str
    temp_range_c: protocols.TempRange
    avg_temp_c: float
    chance_of_precip: float
    max_wind_kph: float
