import datetime

import protocols

class DailyForecast:
    """Represents a daily forecast."""
    def __init__(self, date: datetime.date, temp_range_c: protocols.TempRange):
        """Initializes a DailyForecast object."""
        self.date = date
        self.temp_range_c = temp_range_c

    @property
    def max_temp_c(self) -> int:
        """Returns the maximum temperature for the day in celsius."""
        return self.temp_range_c.max
    
    @property
    def min_temp_c(self) -> int:
        """Returns the minimum temperature for the day in celsius."""
        return self.temp_range_c.min