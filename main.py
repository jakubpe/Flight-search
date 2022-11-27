#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import data_manager
import flight_data
import flight_search

# data_object = data_manager.DataManager()
flight_codes = flight_search.FlightSearch()
data_configurer = flight_data.FlightData()

"""It was run and the excel was updated with iataCodes,
change was introduced to data_manager.DataManager(), method get_all_excel() was run one time in __init__ and now is 
changed to function to be run independently that's why it is nowhere to be seen in below code"""
# for row in data_object.data["prices"]:
#     city = row["city"]
#     row["iataCode"] = flight_codes.get_iata(city)
#     # print(row)
#
# print(data_object.data)
# print("\n-----------------------UPDATE TO THE EXCEL--------------------------------------\n")
# data_object.update_excel(data_object.data)
"""end of what was run successfully"""

flight_info = flight_codes.serach_flights()
data_configurated = data_configurer.configure_flights(flight_info)
data_configurer.print_flights(data_configurated)
