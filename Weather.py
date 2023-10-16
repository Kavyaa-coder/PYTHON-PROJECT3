import tkinter as tk
from tkinter import ttk
import requests
import json

# Replace with your OpenWeatherMap API key
API_KEY = "2cb738a69d8915d2219f7d15398002ff"

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = json.loads(response.text)

        if data["cod"] == 200:
            weather = data["weather"][0]["main"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind_speed = data["wind"]["speed"]

            result_text.set(f"Weather: {weather}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nPressure: {pressure} hPa\nWind Speed: {wind_speed} m/s")
        else:
            result_text.set("City not found")
    except Exception as e:
        result_text.set(f"An error occurred: {str(e)}")

def get_weather_info():
    city = city_entry.get()
    if city:
        get_weather(city)

# Create a GUI window
window = tk.Tk()
window.title("Weather App")

# Create and configure GUI components
style = ttk.Style()
style.configure("TButton", padding=10, relief="flat", background="#0078d4", foreground="white")
style.configure("TLabel", padding=10, font=("Helvetica", 14), anchor="center")

city_label = ttk.Label(window, text="Enter City:")
city_entry = ttk.Entry(window)
get_weather_button = ttk.Button(window, text="Get Weather", command=get_weather_info)

result_text = tk.StringVar()
result_label = ttk.Label(window, textvariable=result_text, wraplength=300, justify="center")

# Place components on the window
city_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
city_entry.grid(row=0, column=2, padx=10, pady=10, columnspan=2)
get_weather_button.grid(row=1, column=1, padx=10, pady=10)
result_label.grid(row=2, column=0, padx=10, pady=10, columnspan=4)

# Start the GUI event loop
window.mainloop()
