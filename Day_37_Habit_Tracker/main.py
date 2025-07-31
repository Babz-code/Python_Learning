import requests
import datetime as dt

with open("secret.txt", "r") as file:
    new = file.readlines()

MY_URL = "https://pixe.la/v1/users"
TOKEN = new[0]


req_body = {
    "token": TOKEN,
    "username": "tbabz",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# create a username
# response = requests.post(url=MY_URL, json=req_body)
# print(response.text)

graph_endpoint = f"{MY_URL}/tbabz/graphs"

graph_params = {
    "id": "graph1",
    "name": "Study Tracker",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}

HTTP_HEADER = {
    "X-USER-TOKEN": TOKEN
}

# # create graph
# response = requests.post(url=graph_endpoint, json=graph_params, headers=HTTP_HEADER)
# print(response.text)

today = dt.datetime(year=2025, month=7, day=30)

pixel_endpoint = f"{graph_endpoint}/graph1"

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20"
}

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=HTTP_HEADER)
# print(response.text)

# update pixels
update_endpoint = f"{pixel_endpoint}/20250730"
params = {
    "quantity": "15"
}

response = requests.put(url=update_endpoint, json=params, headers=HTTP_HEADER)
print(response.text)