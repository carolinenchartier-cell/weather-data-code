import requests
from rich import print
from datetime import datetime

def display_current_weather(city):
  """Displays the current weather"""
  api_key = "0fa35b0t8477d72d0f1c0ad4ba3fo913"
  api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"
  response = requests.get(api_url)
  current_weather_data = response.json()

  if response.status_code == 200 and current_weather_data.get('temperature'):
    current_weather_city = current_weather_data['city']
    current_weather_temperature = current_weather_data['temperature']['current']
    current_weather_temperature = round(current_weather_temperature)
    print(f"The temperature in {current_weather_city} is {current_weather_temperature}C")
  else:
    print(f"Could not retrieve weather for {city}. Response: {current_weather_data.get('message', 'Unknown error')}")

def display_forecast_weather(city):
  """Displays the forecast weather"""
  api_key = "0fa35b0t8477d72d0f1c0ad4ba3fo913"
  api_url= f"https://api.shecodes.io/weather/v1/forecast?query={city}&key={api_key}" # Changed city_name to city

  response = requests.get(api_url)
  forecast_weather_data = response.json()
  # print(forecast_weather_data) # This can be uncommented for debugging if needed

  for day in forecast_weather_data['daily']: # Moved loop inside the function
    timestamp = day['time']
    temperature = day['temperature']['day']
    date = datetime.fromtimestamp(timestamp)
    formatted_day = date.strftime("%A, %B %d")
    print (formatted_day)
    print(f"{formatted_day}: {round(temperature)}C")

city_name = input("Enter a city: ")
city_name = city_name.strip()

if city_name:
  display_current_weather(city_name)
  display_forecast_weather(city_name)
else:
  print("Please try again and enter a city name.")
