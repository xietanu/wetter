"""Provides a function to get a MultiDayForecast for a given location."""
import caching
import protocols
import forecast


def get_forecast(
    location: str,
    requester: protocols.CachedWeatherRequester = caching.get_forecast_data,
) -> protocols.MultiDayForecast:
    """Returns a MultiDayForecast for the given location and number of days."""
    data = requester(location, invalidation_time_hrs=3)
    return forecast.MultiDayForecast.from_json(data)
