import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.token = {}

    def get_token(self):
        # TODO 2. Get Authorization Token
        TOKEN_EP = os.getenv('TOKEN_EP')

        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": os.getenv("API_KEY"),
            "client_secret": os.getenv("API_SECRET")
        }
        response = requests.post(url=TOKEN_EP, headers=header, data=body)
        response.raise_for_status()
        new_response = response.json()
        self.token = new_response['access_token']



    def get_iatacode(self, city):
        # TODO 3. Get iataCode using amadeus API
        self.get_token()
        CITY_CODE_EP = os.getenv("CITY_CODE_EP")

        auth_token = {
            "Authorization": f"Bearer {self.token}"
        }

        parameters = {
            "keyword": f"{city}",
            "max": 1
        }
        response = requests.get(CITY_CODE_EP, params=parameters, headers=auth_token)
        try:
            iatacode = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"
        return iatacode


    def get_flight_update(self, origin_city, destination_city, is_direct = True):
        self.get_token()
        FLIGHT_SEARCH_EP = os.getenv("FLIGHT_SEARCH_EP")

        tomorrow = datetime.now() + timedelta(days=1)
        six_month = tomorrow + timedelta(days=180)

        auth_header = {
            "Authorization": f"Bearer {self.token}"
        }

        parameters = {
            "originLocationCode": f"{origin_city}",
            "destinationLocationCode": f"{destination_city}",
            "departureDate": f"{tomorrow.strftime("%Y-%m-%d")}",
            "returnDate": f"{six_month.strftime("%Y-%m-%d")}",
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": 10
        }

        response = requests.get(FLIGHT_SEARCH_EP, params=parameters, headers=auth_header)
        if response.status_code != 200:
            print(f"The flight's response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None
        return response.json()




