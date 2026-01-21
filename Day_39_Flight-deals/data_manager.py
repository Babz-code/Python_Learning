import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

PRICES_EP = os.getenv('PRICES_EP')
USERS_EP = os.getenv('USERS_EP')

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        # TODO 1. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(PRICES_EP)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data


    def get_email(self):
        response = requests.get(USERS_EP)
        data = response.json()
        self.user_data = data["users"]
        return self.user_data

    def edit_rows(self, num, city_code):
        #  TODO 4. Edit and update the Google sheet with the iataCode using Sheety API
        parameters = {
            "price": {
                "iataCode": f"{city_code}"
            }
        }

        response = requests.put(url=f"{PRICES_EP}/{num}", json=parameters)
        response.raise_for_status()