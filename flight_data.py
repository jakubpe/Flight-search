import flight_search

class FlightData:
    """This class is responsible for structuring the flight data."""
    def __init__(self):
        pass

    def flight_back(self, route):
        """route is a dictionary with key value 'route'"""
        if len(route["route"]) == 2:
            departure = route["route"][1]["local_departure"]
            date_time = departure[:10] + " " + departure[11:16]
            return date_time

        if len(route["route"]) == 4:
            departure = route["route"][3]["local_departure"]
            date_time = departure[:10] + " " + departure[11:16]
            return date_time

    def configure_flights(self, data):
        """data is in form of a dictionary, key value here is 'data' which contains a list of dictionaries
        each representing a possible flight, below code configures that data to easy to digest string"""

        data_configured = {}
        for item in data:
            city_data = data[item]["data"]
            if len(city_data) == 0:
                print(f"No good flights from Warsaw to {str(item)}\n-------------------------------------")
            else:
                for flight in city_data:
                    # if len(flight["route"]) == 2:
                    cost = flight["price"]
                    departure = flight["route"][0]["local_departure"]
                    date_time = departure[:10] + " " + departure[11:16]
                    # print(f"From Gdansk to {str(item)} costs {cost}, departure at {date_time}")
                    flight_back = self.flight_back(flight)
                    item_to_add = {}
                    """Number of landings == 2 means that the flight is directly connected, 4 is with one stop etc"""
                    item_to_add[item] = {
                        "departure": "Warsaw",
                        "arrival": str(item),
                        "cost": cost,
                        "departure_time": date_time,
                        "number_of_landings": len(flight["route"]),
                        "flight_back_time": flight_back
                    }
                    try:
                        if cost > data_configured[item]["cost"]:
                            pass
                        else:
                            data_configured[item]["cost"] = cost
                            data_configured[item]["departure_time"] = date_time
                    except:
                        data_configured[item] = item_to_add[item]

        return data_configured

    def print_flights(self, flights):
        """flights is a dictionary containing data in this format:
            {
                "Paris": {
                    "departure": "Warsaw",
                    "arrival": "Paris",
                    "cost": 230,
                    "departure_time": "2023-01-10 06:30",
                    "number_of_landings": 2,
                    "flight_back_time": "2023-01-17 09:15",
                         },
        """
        for key in flights:
            destination = str(key)
            departure = flights[key]["departure"]
            departure_time = flights[key]["departure_time"]
            flight_back = flights[key]["flight_back_time"]
            cost = flights[key]["cost"]
            print(f"Flight from {departure} to {destination} costs {cost}"
                  f"\nDeparture time: {departure_time}\nFlight back time: {flight_back}\n----------------------------")




            # city_from = item["cityFrom"]
            # city_to = item["cityTo"]
            # price = item["price"]
            # link = item["deep_link"]
            # item_to_add = f"From {city_from} to {city_to} costs {price}\nlink - its a deep link it doesnt showup, its shy"
            # data_configured.append(item_to_add)
            # print(item_to_add)


# testing = flight_search.FlightSearch()
# flight_data_dict = testing.serach_flights()
# testingv = FlightData()
# testingv.configure_flights(flight_data_dict)


