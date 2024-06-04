from weather_api import WeatherAPI


class WeatherForecast:
    def __init__(self):
        self.weather_api = WeatherAPI()

    def get_detailed_forecast(self, city):
        data = self.weather_api.fetch_weather_data(city)
        return self.weather_api.parse_weather_data(data)

    def display_weather(self, city):
        data = self.weather_api.fetch_weather_data(city)
        if not data:
            return f"Weather data not available for {city}"
        else:
            return self.weather_api.parse_weather_data(data)

