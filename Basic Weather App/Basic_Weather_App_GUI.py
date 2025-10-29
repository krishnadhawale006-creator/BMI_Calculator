import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO

API_KEY = "f5a6706add51aee836b0fa8970b6a1f8"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        show_weather(data)
    else:
        messagebox.showerror("Error", "City not found!")

def show_weather(data):
    city_name = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    condition = data['weather'][0]['description'].title()
    icon_code = data['weather'][0]['icon']

    # Fetch weather icon
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    icon_response = requests.get(icon_url)
    icon_image = Image.open(BytesIO(icon_response.content))
    icon_photo = ImageTk.PhotoImage(icon_image)

    icon_label.config(image=icon_photo)
    icon_label.image = icon_photo

    result_label.config(
        text=f"{city_name}, {country}\n"
             f"Temperature: {temp}°C\n"
             f"Humidity: {humidity}%\n"
             f"Condition: {condition}"
    )

# GUI setup
root = tk.Tk()
root.title("Weather App 🌤")
root.geometry("400x400")
root.resizable(False, False)

tk.Label(root, text="Weather App", font=("Arial", 16, "bold")).pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12), justify="center")
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather, bg="#4CAF50", fg="white").pack(pady=10)

icon_label = tk.Label(root)
icon_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
