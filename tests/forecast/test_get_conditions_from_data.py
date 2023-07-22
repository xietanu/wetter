import json
from typing import Any

import protocols
from forecast import get_conditions_from_data


def get_example_data() -> dict[str, Any]:
    """Returns example data from a file."""
    with open(
        "./tests/forecast/example_conditions_data.json", "r", encoding="utf-8"
    ) as file:
        return json.load(file)


def test_get_conditions_from_data():
    """Tests the get_conditions_from_data function."""
    example_data = get_example_data()
    conditions = get_conditions_from_data(example_data)

    assert isinstance(conditions, protocols.Conditions)
    assert conditions.description == "Partly cloudy"
    assert conditions.temp_c == 19.0
    assert conditions.feels_like_c == 17.2
    assert conditions.wind_speed_kph == 5.5
