import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "691011b732213b48da6c0d9657639d2d"

weather_params = {
    "lat": 36.162663,
    "lon": -86.781601,
    "appid": api_key,
    "cnt": 4,
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
print(response.status_code)
print(response.json())

weather_data = response.json()

# question_data = (data["results"])
# print(weather_data["list"][0]["weather"][0]["id"])

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        # print("Bring an umbrella!")
        will_rain = True

if will_rain:
    print("Bring Umbrella")
else:
    print("No Umbrella needed.")


# if code <= sunset or time_now <= sunrise: