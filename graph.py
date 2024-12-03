import matplotlib.pyplot as plt
import json
import os

# Define the path to the weather data file
file_path = os.path.join("static_data", "weather_data.json")

# Load weather data from the JSON file
with open(file_path, "r") as file:
    weather_data = json.load(file)

# Extract data for plotting
dates = [entry["date"] for entry in weather_data["daily_forecast"]]
day_temp = [entry["temperature"]["day"] for entry in weather_data["daily_forecast"]]
min_temp = [entry["temperature"]["min"] for entry in weather_data["daily_forecast"]]
max_temp = [entry["temperature"]["max"] for entry in weather_data["daily_forecast"]]

# Plot weather data
plt.figure(figsize=(10, 6))
plt.plot(dates, day_temp, label="Day Temperature", marker="o")
plt.plot(dates, min_temp, label="Min Temperature", marker="o")
plt.plot(dates, max_temp, label="Max Temperature", marker="o")
plt.title("5-Day Weather Forecast for Los Angeles, CA")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
