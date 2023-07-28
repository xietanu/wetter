"""Represents the weather conditions at a given time."""

from typing import Protocol


class Conditions(Protocol):
    """Represents the weather conditions at a given time."""

    description: str
    temp_c: float
    feels_like_c: float
    wind_speed_kph: float
