"""Types for API requests."""
from typing import Any, Protocol


class WeatherRequester(Protocol):
    """Protocol for weather requests."""

    def __call__(self, location: str, **kwargs) -> dict[str, Any]:  # type: ignore
        """Returns the weather as a dictionary."""
