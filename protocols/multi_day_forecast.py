"""Defines the MultiDayForecast protocol."""
from __future__ import annotations
from typing import Protocol

import datetime
import protocols


class MultiDayForecast(Protocol):
    """Forecast for multiple days."""
    location: str

    def get_available_dates(self) -> list[datetime.date]:  # type: ignore
        """Returns a list of available dates for the forecast."""
 
    def __getitem__(self, key: datetime.date) -> protocols.DailyForecast:  # type: ignore
        """Returns the forecast for a given date."""
