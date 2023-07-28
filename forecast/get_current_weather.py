"""Contains the DailyForecast class for representing a daily forecast."""
import protocols
import caching
import forecast


def get_current_weather(
    location: str,
    source: protocols.CachedWeatherRequester = caching.get_current_weather_data,
) -> protocols.Conditions:
    """Returns the current weather."""
    cache_dict = source(
        location=location,
        invalidation_time_hrs=1,
        cache_location="./cache/",
    )

    return forecast.Conditions.from_json(cache_dict[forecast.CURRENT_WEATHER])
