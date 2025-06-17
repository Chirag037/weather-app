import requests
from config import API_KEY

def get_weather_by_city():
    city = input("Enter city name: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    fetch_and_display_weather(url)

def get_weather_by_coords():
    try:
        lat = float(input("Enter latitude: "))
        lon = float(input("Enter longitude: "))
    except ValueError:
        print("❌ Invalid coordinates. Please enter numbers.")
        return
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    fetch_and_display_weather(url)

def fetch_and_display_weather(url):
    try:
        print(f"🔍 Requesting: {url}")  # Debug print

        response = requests.get(url)
        print("🔁 Status Code:", response.status_code)
        print("📦 Response Text:", response.text)

        if response.status_code != 200:
            print("❌ Failed to fetch weather data. Please check your input or API key.")
            return

        data = response.json()

        name = data.get("name", "Unknown location")
        country = data["sys"].get("country", "")
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n📍 {name}, {country}")
        print(f"🌤  Weather: {weather}")
        print(f"🌡  Temperature: {temp}°C")
        print(f"💧  Humidity: {humidity}%")
        print(f"💨  Wind Speed: {wind_speed} m/s\n")

    except Exception as e:
        print("⚠️ Error:", e)

def main():
    while True:
        print("🌦️ Weather CLI App")
        print("1. Get weather by city name")
        print("2. Get weather by coordinates")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            get_weather_by_city()
        elif choice == "2":
            get_weather_by_coords()
        elif choice == "3":
            print("👋 Exiting. Have a nice day!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

input("Press Enter to exit...")

