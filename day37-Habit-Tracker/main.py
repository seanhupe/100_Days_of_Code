import requests
from datetime import datetime

USERNAME = "seanhupe"
TOKEN = "asaldkfjghakdjf"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

uers_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=uers_params)
# print(response.text)
# -------------------------------------------------------------------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "m",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# -----------------------------------------------------------------------

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2024, month=10, day=28)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "18",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# -------------------------------------------------------------------
## UPDATE
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4.5",
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response.text).................
# -------------------------------------------------------------------------
## DELETE
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
