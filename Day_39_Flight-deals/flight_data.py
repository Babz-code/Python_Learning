import requests
import os

class FlightData:
    # This initially takes in the first flight data
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def find_cheapest_flight(data):
    if data is None or not data['data']:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = data['data'][0]
    first_price = float(first_flight["price"]["grandTotal"])
    origin_airport = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    last_airport = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    number_of_stops = len(first_flight["itineraries"][0]["segments"])

    cheap_flight = FlightData(first_price, origin_airport, last_airport, out_date, return_date, number_of_stops)

    for travel in data["data"]:
        new_price = float(travel["price"]["grandTotal"])
        if new_price < first_price:
            # Data is updated to the info of the lowest price
            first_price = new_price
            origin_airport = travel["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            last_airport = travel["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = travel["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = travel["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            number_of_stops = len(travel["itineraries"][0]["segments"])
            cheap_flight = FlightData(first_price, origin_airport, last_airport, out_date, return_date, number_of_stops)
    print(f"Lowest price to {last_airport} is £{first_price}")
    return cheap_flight





