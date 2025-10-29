import requests

# Get your free API key from https://openweathermap.org/api
API_KEY = "f5a6706add51aee836b0fa8970b6a1f8"  # Replace with your own key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"\n🌍 Weather in {data['name']}, {data['sys']['country']}")
        print(f"🌡 Temperature: {data['main']['temp']}°C")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"🌤 Condition: {data['weather'][0]['description'].title()}")
    else:
        print("❌ City not found or error fetching data!")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
