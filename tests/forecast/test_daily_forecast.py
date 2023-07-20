import protocols
import datetime
from forecast import daily_forecast

def create_example_forecast() -> daily_forecast.DailyForecast:
    """Creates an example forecast for testing."""
    date = datetime.date(2023, 1, 1)
    temp_range_c = protocols.TempRange(0, 10)
    return daily_forecast.DailyForecast(date, temp_range_c)

def test_daily_forecast_date():
    assert create_example_forecast().date == datetime.date(2023, 1, 1)

def test_daily_forecast_max_temp_c():
    assert create_example_forecast().max_temp_c == 10

def test_daily_forecast_min_temp_c():
    assert create_example_forecast().min_temp_c == 0