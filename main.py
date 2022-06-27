import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "76aa0d3f7a72b814b612b6f4532811bc"

weather_params = {
    "lat": 39.575500,
    "lon": -106.100400,
    "appid": api_key,
}


response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
