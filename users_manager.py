import requests


SHEETY_API_USERS_ENDPOINT = "https://api.sheety.co/e204560bf45633f6dae1833c5243df7f/flightDeals/users"
HEADERS = {
    "Authorization": "Auth_token_get_your_own"
}


class Fligt_Club:
    """manages the users sheet"""
    def __init__(self):
        pass

    def add_user(self):
        print("Welcome")
        name = input("What is your name?: ")
        last_name = input("What is your last name?: ")
        email_info = input("What is your email? :")
        email_check = input("Type your email again: ")
        while email_info != email_check:
            print("Emails dont match, please provide them again:")
            email_info = input("What is your email? :")
            email_check = input("Type your email again: ")

        data = {
            "user": {
                    "firstName": name,
                    "lastName": last_name,
                    "email": email_info,
                    "id": 2
            }
        }

        # print(data)
        response = requests.post(url=SHEETY_API_USERS_ENDPOINT, json=data, headers=HEADERS)
        print(response.raise_for_status())
        print(response.text)

testing = Fligt_Club()
testing.add_user()



