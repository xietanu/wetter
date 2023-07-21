import datetime
import json
import os

import api
import caching
import protocols


def update_cache(
    cache_name: str,
    location: str,
    weather_requester: protocols.WeatherRequester,
    cache_location: str = "./cache/",
):
    """Updates the cache with the current weather."""
    if not os.path.exists(cache_location):
        os.mkdir(cache_location)

    cache_file_path = cache_location + cache_name + "_" + location.lower() + ".json"

    weather_dict = weather_requester(location)

    weather_dict["cache_time"] = str(datetime.datetime.now())

    with open(cache_file_path, "w", encoding="utf-8") as cache_file:
        json.dump(weather_dict, cache_file)


def update_current_weather_cache(location: str):
    """Updates the current weather cache."""
    update_cache(
        cache_name=caching.CURRENT_WEATHER_CACHE_NAME,
        location=location,
        weather_requester=api.get_current_weather,
    )


def update_forecast_cache(location: str):
    """Updates the forecast cache."""
    update_cache(
        cache_name=caching.FORECAST_CACHE_NAME,
        location=location,
        weather_requester=api.get_forecast,
    )
