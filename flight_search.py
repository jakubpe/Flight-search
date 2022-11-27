import requests
from datetime import date, timedelta


URL = "https://api.tequila.kiwi.com/locations/query"
HEADERS = {
    "apikey": "Auth_token_get_your_own"
}

future_date = date.today() + timedelta(days=180)
FUTURE_DATE = future_date.strftime("%d/%m/%Y")

today_date = date.today()
TODAY = today_date.strftime("%d/%m/%Y")


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_iata(self, city):
        """This fetches iata codes for the cities in the excel file, it was run, in case a user adds new cities
        to the excel only then it is supposed to be run again"""
        parameters = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=URL, params=parameters, headers=HEADERS)
        data = response.json()
        iata_code = data["locations"][0]["code"]
        return iata_code

    def serach_flights(self):
        """searches all flights for the delivered parameters, which are to be delivered as a dictionary - 'params',
        data delivered is in form of dictionary and the first key is the name of the sheet, in this case 'prices'
        value for the key prices is a list of all the rows of the excel, each item in the list is a dictionary
        represented like that:
        {"city": "Paris",
         "iataCode": "PAR",
          "lowestPrice": 54,
           "id": 2},
        id is a number of row, the lowest price is there to use as a filter for searching good deals, iatacodes are
        used to search filghts - one of the keys for the kiwi api, """
        #this data is pasted to limit requests to sheety api, there is a limit of request for no-paying guys like me

        """,         
                  
                                                 
                     just making data_list shorter for testing"""

        data_list = [
            {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 250, 'id': 2},
            {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 400, 'id': 3},
            {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 4500, 'id': 4},
            {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 10000, 'id': 5},
            {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 800, 'id': 6},
            {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 5000, 'id': 7},
            {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 2400, 'id': 8},
            {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 3000, 'id': 9}

        ]

        # data_list = params["prices"] params to be added in definition
        search_endpoint = "https://api.tequila.kiwi.com/v2/search"

        dict_of_flights = {}
        for item in data_list:
            flight_parameters = {
                "fly_from": "WAW",
                "fly_to": item["iataCode"],
                "date_from": TODAY,
                "date_to": FUTURE_DATE,
                "curr": "PLN",
                "price_to": item["lowestPrice"],
                "max_stopovers": 2,
                "nights_in_dst_from": 5,
                "nights_in_dst_to": 7,
            }

            response = requests.get(url=search_endpoint, params=flight_parameters, headers=HEADERS)
            # print(response.raise_for_status)
            # print(response.text)
            dict_of_flights[item["city"]] = response.json()
        """now it responds nicely, if the return data is none then probably no flights in this price range or
        change the max_stopovers as there arent many direct flights from Gdansk"""
        """The next step is to transfer the data to flight_data.py to configure it into digestible form, 
        step after that is to do the whole job in the main.py, extra points if i am able to change the max_stopovers
        and figure out how to present data no matter how many steps in the flight, another extra point if
        i figure out how to look for flights back"""
        # print(response.text)
        # return response.json()
        return dict_of_flights

    def filter_flights(self, flights_dict):
        """Filters flights by price, it occured that the kiwi appi has a price_to param, rendering this function
        expendable"""
        price = 200
        flights_list = []
        options = flights_dict["data"]
        # print(options)
        for item in options:
            if int(item["price"]) <= price:
                flights_list.append(item)

        return flights_list


# testing = FlightSearch()
# data = testing.serach_flights()
# print(data)


# print(options)
# data_filtered = testing.filter_flights(data)
# data_configured = []

# for item in options:
#     city_from = item["cityFrom"]
#     city_to = item["cityTo"]
#     price = item["price"]
#     link = item["deep_link"]
#     item_to_add = f"From {city_from} to {city_to} costs {price}\nlink - its a deep link it doesnt showup, its shy"
#     data_configured.append(item_to_add)
#     print(item_to_add)



# # print(data_filtered)
# print(len(data_filtered))
# for piece in data_configured:
#     print(piece)