import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "76aa0d3f7a72b814b612b6f4532811bc"

weather_params = {
    "lat": 39.575500,
    "lon": -106.100400,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an unbrella.")

# print(weather_data["hourly"][0]["weather"][0]["id"])
