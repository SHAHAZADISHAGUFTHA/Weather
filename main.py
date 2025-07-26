import requests
from tkinter import *

# Replace with your actual OpenWeatherMap API key
API_KEY = "cde87e31f8b2ecdb5efdf549f01d10a6"  # Fixed curly quotes

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(base_url, params=params)
    return response.json()

def show_weather():
    city = city_entry.get()
    weather = get_weather(city)

    if weather.get("cod") != 200:
        result_label.config(text="City not found.")
    else:
        temp = weather["main"]["temp"]
        desc = weather["weather"][0]["description"].capitalize()
        humidity = weather["main"]["humidity"]
        wind = weather["wind"]["speed"]

        result = (
            f"City: {city}\n"
            f"Temperature: {temp}°C\n"
            f"Weather: {desc}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} m/s"
        )
        result_label.config(text=result)

# Tkinter GUI setup
root = Tk()
root.title("🌤️ Weather App")
root.geometry("460x400")
COLOR_BG = "#add8e6"
root.configure(bg=COLOR_BG)

# --- Centering everything ---
container = Frame(root, bg=COLOR_BG)
container.pack(expand=True)  # Center the container vertically & horizontally

Label(container, text="Enter city name:", font=("Arial", 15), bg=COLOR_BG).pack(pady=5)
city_entry = Entry(container, width=30)
city_entry.pack(pady=5)

Button(container, text="Get Weather", command=show_weather).pack(pady=10)

# Result label (same background)
result_label = Label(container, text="", font=("Arial", 15), justify=LEFT, bg=COLOR_BG)
result_label.pack(pady=10)

root.mainloop()