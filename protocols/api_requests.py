"""Types for API requests."""
from typing import Any, Callable


WeatherRequester = Callable[[str], dict[str, Any]]
