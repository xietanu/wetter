"""Module for protocols."""
from protocols.type_names import TempRange
from protocols.daily_forecast import DailyForecast
from protocols.multi_day_forecast import MultiDayForecast
from protocols.api_requests import WeatherRequester, CachedWeatherRequester
from protocols.conditions import Conditions
