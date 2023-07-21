from __future__ import annotations
from typing import Protocol

import datetime
import protocols


class MultiDayForecast(Protocol):
    def get_available_dates(self) -> list[datetime.date]:  # type: ignore
        """Returns a list of available dates for the forecast."""

    def get_daily_forecast(self, date: datetime.date) -> protocols.DailyForecast:  # type: ignore
        """Returns the forecast for a given date."""
