import requests

# Your OpenWeatherMap API key
API_KEY = "659bed194bc464cc702eafeb0d57a539"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

print("Welcome to the Basic Weather App!")
city = input("Enter city name: ")

# Construct the full API URL with user input
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

# Send GET request to the weather API
response = requests.get(url)
data = response.json()

# Check if the request was successful
if response.status_code == 200 and data.get("cod") == 200:
    # Extract relevant weather information
    weather = data["weather"][0]["description"].capitalize()
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    # Print weather details
    print(f"\nWeather in {city}:")
    print(f"Condition: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    # Print the error message returned by the API
    print(f"\nCity not found. Please check the spelling and try again.")
    print(f"Details: {data.get('message', 'No details available.')}")
