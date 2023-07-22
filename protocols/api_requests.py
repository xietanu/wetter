"""Types for API requests."""
from typing import Any, Protocol


class WeatherRequester(Protocol):
    """Protocol for weather requests."""

    def __call__(self, location: str, **kwargs) -> dict[str, Any]:  # type: ignore
        """Returns the weather as a dictionary."""


class CachedWeatherRequester(Protocol):
    """Protocol for cached weather requests."""

    def __call__(
        self,
        location: str,
        invalidation_time_hrs: int,
        cache_location: str = "./cache/",
    ) -> dict[str, Any]:  # type: ignore
        """Returns the weather as a dictionary."""
