"""Represents the forecast for a single day."""
from __future__ import annotations
import datetime
import forecast
import protocols


class DailyForecast:
    """Represents the forecast for a single day."""

    def __init__(
        self,
        date: datetime.date,
        summary: protocols.DaySummary,
        hours: list[protocols.Conditions],
    ):
        self._date = date
        self._summary = summary
        self._hours = hours

    @classmethod
    def from_json(cls, json: dict) -> DailyForecast:
        """Returns a DailyForecast from a JSON response."""
        return cls(
            date=datetime.date.fromisoformat(json[forecast.DATE]),
            summary=forecast.DaySummary.from_json(json),
            hours=[
                forecast.Conditions.from_json(hour) for hour in json[forecast.HOURS]
            ],
        )

    @property
    def date(self) -> datetime.date:
        """Returns the date of the forecast."""
        return self._date

    @property
    def summary_description(self) -> str:
        """Returns the summary description of the forecast."""
        return self._summary.description

    @property
    def temp_range_c(self) -> protocols.TempRange:
        """Returns the temperature range of the forecast."""
        return self._summary.temp_range_c

    @property
    def avg_temp_c(self) -> float:
        """Returns the average temperature of the forecast."""
        return self._summary.avg_temp_c

    @property
    def chance_of_precip(self) -> float:
        """Returns the chance of precipitation for the forecast."""
        return self._summary.chance_of_precip

    @property
    def max_wind_kph(self) -> float:
        """Returns the maximum wind speed for the forecast."""
        return self._summary.max_wind_kph

    def __getitem__(self, key: int | datetime.time) -> protocols.Conditions:
        """Returns the conditions for a given time."""
        if isinstance(key, int):
            return self._hours[key]
        return self._hours[key.hour]

    def __len__(self) -> int:
        """Returns the number of hours in the forecast."""
        return len(self._hours)

    def __contains__(self, key: int | datetime.time) -> bool:
        """Returns whether the forecast contains a given time."""
        if isinstance(key, int):
            return 0 <= key < len(self)
        return key.hour < len(self)

    def __iter__(self):
        """Returns an iterator over the conditions for each hour in the forecast."""
        return iter(self._hours)