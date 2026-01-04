# collector.py - Collects data from OpenWeatherMap, handles errors, and logs data.

import requests
import pandas as pd
import time
import json
import os # We need the os module to check if the file exists

# --- CONFIGURATION ---
# IMPORTANT: Replace the placeholder with your actual OpenWeatherMap API Key
API_KEY = "55bd1147f6b36a437aa7712ff32c5336" # NOTE: This key is now exposed, but you should use your actual working key
CITY_NAME = "Colombo, LK"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
HISTORY_FILE = 'weather_history.csv'

def fetch_weather_data():
    """Fetches current weather data and logs it to a CSV file."""
    print(f"\n--- Starting Data Fetch for {CITY_NAME} ---")

    params = {
        'q': CITY_NAME,
        'appid': API_KEY,
        'units': 'metric' # Use Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params)

        # Print the status code for immediate feedback
        print(f"API Response Status Code: {response.status_code}")

        # This will raise an exception (go to the except block) if the status is 4xx or 5xx
        response.raise_for_status()

        # If we reach here, the connection was successful (Status 200)
        data = response.json()

        # --- Data Processing and Selection ---
        timestamp = time.time()
        temp_c = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_desc = data['weather'][0]['description']

        # Create a simple DataFrame for the new data point
        new_data = pd.DataFrame([{
            'timestamp': timestamp,
            'time_readable': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp)),
            'temperature_c': temp_c,
            'humidity_percent': humidity,
            'wind_speed_m_s': wind_speed,
            'description': weather_desc
        }])

        # Append data to a CSV file (your data log)
        if os.path.exists(HISTORY_FILE):
            # Read existing data and append the new row
            history_df = pd.read_csv(HISTORY_FILE)
            history_df = pd.concat([history_df, new_data], ignore_index=True)
        else:
            # If the file doesn't exist, use the new data frame
            history_df = new_data

        history_df.to_csv(HISTORY_FILE, index=False)
        print(f"SUCCESS: Data saved to {HISTORY_FILE}!")
        print(f"Current Conditions: Temp={temp_c}°C, Humidity={humidity}%")

    except requests.exceptions.HTTPError as e:
        print(f"\n--- FAILED TO CONNECT (HTTP Error) ---")
        print(f"Details: {e}")
        print(f"Status: {e.response.status_code}. Please check your API Key and City Name configuration.")
    except Exception as e:
        print(f"\n--- FAILED TO CONNECT (General Error) ---")
        print(f"An unexpected error occurred: {e}")

# This standard structure ensures the function is called when the script is run directly
if __name__ == "__main__":
    fetch_weather_data()
    print("\n--- Script Finished ---")
