import json

from caching import update_cache


def example_weather_requester(location: str) -> dict[str, str]:
    """Returns an example weather dictionary."""
    return {
        "location": location,
        "date": "2023-01-01",
        "temperature": "10",
        "description": "Sunny",
    }


def test_update_cache():
    update_cache(
        cache_name="test_cache",
        location="London",
        weather_requester=example_weather_requester,
        cache_location="./tests/caching/",
    )

    with open("./tests/caching/test_cache.json", "r", encoding="utf-8") as cache_file:
        cache_dict = json.load(cache_file)

    assert cache_dict == {
        "location": "London",
        "date": "2023-01-01",
        "temperature": "10",
        "description": "Sunny",
    }
