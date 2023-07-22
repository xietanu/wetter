"""Gets the weather for a given location."""
import requests

import api


def get_weather_from_api(
    location: str, endpoint: str, api_key: str = api.API_KEY, **kwargs
) -> dict:
    """Returns the current weather for a given location."""
    url = api.URL_BASE + endpoint

    params = {
        "key": api_key,
        "q": location,
        "aqi": "no",
        "alerts": "no",
    }

    params.update(kwargs)

    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()

    return response.json()


def get_current_weather_from_api(location: str, **kwargs) -> dict:
    """Returns the current weather for a given location."""
    return get_weather_from_api(location, api.CURRENT_WEATHER_ENDPOINT, **kwargs)


def get_forecast_from_api(location: str, days: int, **kwargs) -> dict:
    """Returns the forecast for a given location."""
    return get_weather_from_api(location, api.FORECAST_ENDPOINT, days=days, **kwargs)
