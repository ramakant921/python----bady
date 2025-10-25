import requests

# Your API key from OpenWeatherMap (signup free at https://openweathermap.org/api)
API_KEY = "1044cc8f0fba87d29704e7c38fb718d4"
city = "Delhi"

# API URL with city and key
url = f"http://api.openweathermap.org/data/2.5/weather?q=delhi&appid=1044cc8f0fba87d29704e7c38fb718d4&units=metric"

# Send request
response = requests.get()
data = response.json()

# Check if request was successful
if data["cod"] == 200:
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"🌍 City: {city}")
    print(f"🌤️ Weather: {weather}")
    print(f"🌡️ Temperature: {temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"💨 Wind Speed: {wind_speed} m/s")

else:
    print("❌ Error fetching weather data. Check your API key or city name.")