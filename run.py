import forecast


def main() -> None:
    """Main function."""
    current_weather = forecast.get_current_weather("Düsseldorf")

    print(f"Current weather: {current_weather.description}")
    print(f"Temperature: {current_weather.temp_c}°C")
    print(f"Feels like: {current_weather.feels_like_c}°C")
    print(f"Wind speed: {current_weather.wind_speed_kph}kph")

if __name__ == "__main__":
    main()
