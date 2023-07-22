"""Represents the weather conditions at a given time."""
from dataclasses import dataclass


@dataclass
class Conditions:
    """Represents the weather conditions at a given time."""

    description: str
    temp_c: float
    feels_like_c: float
    wind_speed_kph: float
