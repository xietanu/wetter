"""Defines the MultiDayForecast protocol."""
from __future__ import annotations

import datetime
import protocols
import forecast


class MultiDayForecast:
    """Forecast for multiple days."""

    def __init__(self, location: str, days: list[protocols.DailyForecast]):
        """Initializes the forecast."""
        self.location = location
        self._days = days

    @classmethod
    def from_json(cls, json: dict) -> MultiDayForecast:
        """Returns a MultiDayForecast from a JSON response."""
        return cls(
            location=json[forecast.LOCATION][forecast.NAME],
            days=[
                forecast.DailyForecast.from_json(day)
                for day in json[forecast.FORECAST][forecast.FORECAST_DAY]
            ],
        )

    def get_available_dates(self) -> list[datetime.date]:
        """Returns a list of available dates for the forecast."""
        return [day.date for day in self._days]

    def __getitem__(self, key: datetime.date) -> protocols.DailyForecast:
        """Returns the forecast for a given date."""
        return self._days[self.get_available_dates().index(key)]

    def __len__(self) -> int:
        """Returns the number of days in the forecast."""
        return len(self._days)
