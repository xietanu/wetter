"""Represents the weather conditions at a given time."""
from __future__ import annotations
from dataclasses import dataclass

import forecast


@dataclass
class Conditions:
    """Represents the weather conditions at a given time."""

    description: str
    temp_c: float
    feels_like_c: float
    wind_speed_kph: float

    @classmethod
    def from_json(cls, json: dict) -> Conditions:
        """Returns a Conditions from a JSON response."""
        return cls(
            description=json[forecast.CONDITION_DESC],
            temp_c=json[forecast.TEMP_C],
            feels_like_c=json[forecast.TEMP_FEELS_LIKE_C],
            wind_speed_kph=json[forecast.WIND_KPH],
        )
