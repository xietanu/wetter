from typing import Any
import protocols
import forecast


def get_conditions_from_data(data: dict[str, Any]) -> protocols.Conditions:
    """Returns the current weather."""
    return protocols.Conditions(
        description=data[forecast.CONDITION_DESC][forecast.TEXT_DESC],
        temp_c=data[forecast.TEMP_C],
        feels_like_c=data[forecast.TEMP_FEELS_LIKE_C],
        wind_speed_kph=data[forecast.WIND_KPH],
    )
