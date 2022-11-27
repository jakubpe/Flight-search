import requests
from pprint import pprint
row = int

SHEETY_API_ENDPOINT = "https://api.sheety.co/e204560bf45633f6dae1833c5243df7f/flightDeals/prices"
HEADERS = {
    "Authorization": "Auth_token_get_your_own"
}


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        pass

    def get_all_excel(self):
        """data returned is in form of dictionary and the first key is the name of the sheet, in this case 'prices'
        value for the key prices is a list of all the rows of the excel, each item in the list is a dictionary
        represented like that:
        {"city": "Paris",
         "iataCode": "PAR",
          "lowestPrice": 54,
           "id": 2},
        id is a number of row, the lowest price is there to use as a filter for searching good deals, iatacodes are
        used to search filghts - one of the keys for the kiwi api, """
        response = requests.get(url=SHEETY_API_ENDPOINT, headers=HEADERS)
        # print(response.text)
        return response.json()

    def update_excel(self, dictionary):
        """updates the excel file with iata codes, if new rows with new cities are added then run it
        to update iata codes"""
        for line in dictionary["prices"]:
            row_id = line["id"]
            request_endpoint = f"https://api.sheety.co/e204560bf45633f6dae1833c5243df7f/flightDeals/prices/{row_id}"
            update = {
                "price": {
                    "iataCode": line["iataCode"]
                }
            }
            response = requests.put(url=request_endpoint, json=update, headers=HEADERS)
            print(response.raise_for_status())



# data_manager = DataManager()
# data = data_manager.get_all_excel()
# print(data)

