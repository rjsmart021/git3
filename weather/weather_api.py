# weather_api.py module
class WeatherAPI:

    def __init__(self):
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }

    def add_weather_data(self, city, temperature, condition, humidity):
        self.weather_data[city] = {"temperature": temperature, "condition": condition, "humidity": humidity}

    def fetch_weather_data(self, city):
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city, {})

    def parse_weather_data(self, data):
        if not data:
            return "Weather data not available"
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Temperature is: {temperature} degrees, and condition is: {condition}, Humidity: {humidity}%"

