from __future__ import annotations
from typing import Protocol

import datetime


class DailyForecast(Protocol):
    date: datetime.date

    @property
    def max_temp_c(self) -> int:  # type: ignore
        """Returns the maximum temperature for the day in celsius."""

    @property
    def min_temp_c(self) -> int:  # type: ignore
        """Returns the minimum temperature for the day in celsius."""


class MultiDayForecast(Protocol):
    def get_available_dates(self) -> list[datetime.date]:  # type: ignore
        """Returns a list of available dates for the forecast."""

    def get_daily_forecast(self, date: datetime.date) -> DailyForecast:  # type: ignore
        """Returns the forecast for a given date."""
