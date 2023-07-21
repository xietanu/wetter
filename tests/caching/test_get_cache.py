import pytest
from caching import get_cache


def test_get_cache_file_exists_data_correct():
    expected_data = {
        "location": "London",
        "temperature": "10",
        "description": "Sunny",
        "cache_time": "2020-01-01 04:05:06.0",
    }

    _, actual_data = get_cache(
        cache_name="example_cache",
        location="London",
        cache_location="./tests/caching/",
    )
    assert actual_data == expected_data


def test_get_cache_file_exists_time_correct():
    time, _ = get_cache(
        cache_name="example_cache",
        location="London",
        cache_location="./tests/caching/",
    )

    assert time.year == 2020, "Year is not correct"
    assert time.month == 1, "Month is not correct"
    assert time.day == 1, "Day is not correct"
    assert time.hour == 4, "Hour is not correct"
    assert time.minute == 5, "Minute is not correct"
    assert time.second == 6, "Second is not correct"


def test_get_cache_file_does_not_exist():
    with pytest.raises(FileNotFoundError):
        get_cache(
            cache_name="fake_cache",
            location="Paris",
            cache_location="./tests/caching/",
        )
