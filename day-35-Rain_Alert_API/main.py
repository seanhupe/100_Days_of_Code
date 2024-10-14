import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "691011b732213b48da6c0d9657639d2d"

weather_params = {
    "lat": 36.162663,
    "lon": -86.781601,
    "appid": api_key,
}


response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
response.raise_for_status()
data = response.json()
question_data = (data["results"])