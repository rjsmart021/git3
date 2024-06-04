from weather.weather_forecast import WeatherForecast


def main():
    weather_forecast = WeatherForecast()
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = weather_forecast.get_detailed_forecast(city)
        else:
            forecast = weather_forecast.display_weather(city)
        print(forecast)


if __name__ == "__main__":
    main()