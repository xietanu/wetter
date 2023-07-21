"""Defines the protocols for the daily forecast."""
from __future__ import annotations
from typing import Protocol

import datetime


class DailyForecast(Protocol):
    """Represents the forecast for a single day."""

    date: datetime.date

    @property
    def max_temp_c(self) -> int:  # type: ignore
        """Returns the maximum temperature for the day in celsius."""

    @property
    def min_temp_c(self) -> int:  # type: ignore
        """Returns the minimum temperature for the day in celsius."""
