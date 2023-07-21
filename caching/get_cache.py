import json
import datetime
from typing import Any

import caching

def get_cache(
    cache_name: str,
    location: str,
    cache_location: str = "./cache/",
) -> tuple[datetime.datetime, dict[str, Any]]:
    """Returns the cache as a dictionary."""
    cache_file_path = cache_location + cache_name + "_" + location.lower() + ".json"

    with open(cache_file_path, "r", encoding="utf-8") as cache_file:
        cache_dict = json.load(cache_file)

    cache_time = datetime.datetime.strptime(
        cache_dict["cache_time"], "%Y-%m-%d %H:%M:%S.%f"
    )

    return cache_time, cache_dict

def get_current_weather_cache(
    location: str,
    cache_location: str = "./cache/",
) -> tuple[datetime.datetime, dict[str, Any]]:
    """Returns the current weather cache as a dictionary."""
    return get_cache(
        cache_name=caching.CURRENT_WEATHER_CACHE_NAME,
        location=location,
        cache_location=cache_location,
    )

def get_forecast_cache(
    location: str,
    cache_location: str = "./cache/",
) -> tuple[datetime.datetime, dict[str, Any]]:
    """Returns the forecast cache as a dictionary."""
    return get_cache(
        cache_name=caching.FORECAST_CACHE_NAME,
        location=location,
        cache_location=cache_location,
    )