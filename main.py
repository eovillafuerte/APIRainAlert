import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "place API here"

weather_params = {
    "lat": 39.575500,
    "lon": -106.100400,
    "appid": api_key,
}


response = requests.get(OWM_Endpoint, params=weather_params)
print(response.json())
