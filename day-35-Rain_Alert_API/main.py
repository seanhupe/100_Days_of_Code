import requests

api_key = "691011b732213b48da6c0d9657639d2d"
lat =
lon =

https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=api_key


response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = (data["results"])