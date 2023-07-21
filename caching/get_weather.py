"""Functions for getting weather data from the cache or API."""
import datetime
from typing import Any
import api

import protocols
import caching


def get_weather_dict(
    cache_name: str,
    location: str,
    invalidation_time_hrs: int,
    weather_requester: protocols.WeatherRequester,
    cache_location: str = "./cache/",
    **requester_kwargs,
) -> dict[str, Any]:
    """Returns the current weather as a dictionary."""
    try:
        cache_time, cache_dict = caching.get_cache(
            cache_name=cache_name,
            location=location,
            cache_location=cache_location,
        )
    except FileNotFoundError:
        return _update_and_get_cache(
            cache_name, location, weather_requester, cache_location, **requester_kwargs
        )

    if (
        cache_time + datetime.timedelta(hours=invalidation_time_hrs)
        > datetime.datetime.now()
    ):
        return cache_dict

    return _update_and_get_cache(
        cache_name, location, weather_requester, cache_location, **requester_kwargs
    )


def _update_and_get_cache(
    cache_name, location, weather_requester, cache_location, **requester_kwargs
):
    caching.update_cache(
        cache_name=cache_name,
        location=location,
        weather_requester=weather_requester,
        cache_location=cache_location,
        **requester_kwargs,
    )

    _, cache_dict = caching.get_cache(
        cache_name=cache_name,
        location=location,
        cache_location=cache_location,
    )

    return cache_dict


def get_current_weather(
    location: str,
    invalidation_time_hrs: int,
    cache_location: str = "./cache/",
) -> dict[str, Any]:
    """Returns the current weather as a dictionary."""
    return get_weather_dict(
        cache_name=caching.CURRENT_WEATHER_CACHE_NAME,
        location=location,
        invalidation_time_hrs=invalidation_time_hrs,
        weather_requester=api.get_current_weather,
        cache_location=cache_location,
    )


def get_forecast(
    location: str,
    invalidation_time_hrs: int,
    cache_location: str = "./cache/",
) -> dict[str, Any]:
    """Returns the forecast as a dictionary."""
    return get_weather_dict(
        cache_name=caching.FORECAST_CACHE_NAME,
        location=location,
        invalidation_time_hrs=invalidation_time_hrs,
        weather_requester=api.get_forecast,
        cache_location=cache_location,
        days=3,
    )
