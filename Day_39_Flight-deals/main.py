from pprint import pprint
import time
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

data = DataManager()
flight = FlightSearch()
notice = NotificationManager()

ORIGIN_CITY_IATA = "LON"

sheet_data = data.get_destination_data()
# for row in sheet_data:
#     city_iatacode = flight.get_iatacode(row["city"])
#     data.edit_rows(row["id"], city_iatacode)

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flight_info = flight.get_flight_update(ORIGIN_CITY_IATA, destination["iataCode"])
    the_cheapest = find_cheapest_flight(flight_info)
    print(f"{destination['city']}: £{the_cheapest.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    if the_cheapest.price != "N/A" and the_cheapest.price < destination["lowestPrice"]:
        print(f"Yay! Lower price flight found to {destination['city']}!")

    if the_cheapest.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight.get_flight_update(ORIGIN_CITY_IATA, destination["iataCode"], is_direct=False)
        the_cheapest = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: £{the_cheapest.price} and there are {the_cheapest.stops} stops to destination")

    customer_info = data.get_email()
    email_list = [row["whatIsYourEmail?"] for row in customer_info]
    notice.send_mail(email_list, the_cheapest.origin_airport, the_cheapest.destination_airport, the_cheapest.price)