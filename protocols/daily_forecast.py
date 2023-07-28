"""Defines the protocols for the daily forecast."""
from __future__ import annotations
from typing import Protocol

import datetime

import protocols


class DailyForecast(Protocol):
    """Represents the forecast for a single day."""

    @property
    def date(self) -> datetime.date:  # type: ignore
        """Returns the date of the forecast."""

    @property
    def summary_description(self) -> str:  # type: ignore
        """Returns the summary description of the forecast."""

    @property
    def temp_range_c(self) -> protocols.TempRange:  # type: ignore
        """Returns the temperature range of the forecast."""

    @property
    def avg_temp_c(self) -> float:  # type: ignore
        """Returns the average temperature of the forecast."""

    @property
    def chance_of_precip(self) -> float:  # type: ignore
        """Returns the chance of precipitation for the forecast."""

    @property
    def max_wind_kph(self) -> float:  # type: ignore
        """Returns the maximum wind speed for the forecast."""

    def __getitem__(self, key: int | datetime.time) -> protocols.Conditions:  # type: ignore
        """Returns the conditions for a given time."""

    def __len__(self) -> int:  # type: ignore
        """Returns the number of hours in the forecast."""

    def __contains__(self, key: int | datetime.time) -> bool:  # type: ignore
        """Returns whether the forecast contains a given time."""

    def __iter__(self):
        """Returns an iterator over the conditions for each hour in the forecast."""
