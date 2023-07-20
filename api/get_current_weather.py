"""Gets the current weather for a given location."""
import requests

import api

def get_current_weather(location: str, api_key: str = api.API_KEY) -> dict:
    """Returns the current weather for a given location."""
    params = {
        "key": api_key,
        "q": location,
        "aqi": "no",
        "alerts": "no",
    }
    
    response = requests.get(api.CURRENT_WEATHER_URL, params=params, timeout=5)
    response.raise_for_status()
    
    return response.json()