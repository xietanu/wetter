from __future__ import annotations
from dataclasses import dataclass
import datetime

import protocols
import forecast


@dataclass
class DaySummary:
    """A summary of the weather for a day."""

    date: datetime.date
    description: str
    temp_range_c: protocols.TempRange
    avg_temp_c: float
    chance_of_precip: float
    max_wind_kph: float

    @classmethod
    def from_json(cls, json: dict) -> DaySummary:
        """Returns a DaySummary from a JSON response."""
        return cls(
            date=datetime.date.fromisoformat(json[forecast.DATE]),
            description=json[forecast.DAY][forecast.CONDITION_DESC],
            temp_range_c=protocols.TempRange(
                min=json[forecast.DAY][forecast.MIN_TEMP_C],
                max=json[forecast.DAY][forecast.MAX_TEMP_C],
            ),
            avg_temp_c=json[forecast.DAY][forecast.AVG_TEMP_C],
            chance_of_precip=json[forecast.DAY][forecast.DAILY_CHANCE_OF_RAIN] / 100,
            max_wind_kph=json[forecast.DAY][forecast.MAX_WIND_KPH],
        )
