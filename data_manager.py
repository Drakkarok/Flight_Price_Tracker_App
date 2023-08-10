import requests


class DataManager:
    def __init__(self):
        self.sheety_api_endpoint_get = "address"
        self.sheety_api_endpoint_post = "address"
        self.sheety_api_endpoint_put = "address"
        self.sheety_api_endpoint_delete = "address"
        self.sheety_api_result = None
        self.sheety_api_iata_codes = []
        self.sheety_api_list_of_cities = []
        self.tequila_api_token = "token"
        self.sheety_api_token = "token"
        self.tequila_api_header = {"apikey": self.tequila_api_token}
        self.sheety_api_header = {"Authorization": f"Bearer {self.sheety_api_token}"}

        self.request_data_get()

    def request_data_get(self):
        response = requests.get(url=self.sheety_api_endpoint_get, headers=self.sheety_api_header)
        response.raise_for_status()
        self.sheety_api_result = response.json()
        for city_dict in self.sheety_api_result["sheet1"]:
            self.sheety_api_list_of_cities.append(city_dict["city"])
        self.request_iata_codes()
        self.print()

    def request_iata_codes(self):
        iata_codes_to_find = {}
        for city_dict in self.sheety_api_result["sheet1"]:
            if city_dict["iataCode"] == "":
                iata_codes_to_find[f"{city_dict['city']}"] = city_dict["country"]
            else:
                self.sheety_api_iata_codes.append(city_dict["iataCode"])
        for key in iata_codes_to_find:
            parameters = {
                "term": f"{key}, {iata_codes_to_find[key]}",
                "location_types": "airport"
            }
            response = requests.get(url="https://api.tequila.kiwi.com/locations/query", params=parameters,
                                    headers=self.tequila_api_header)
            response.raise_for_status()
            result = response.json()
            self.sheety_api_iata_codes.append(result["locations"][0]["city"]["code"])

    def print(self):
        print(f"Destinations iata codes: {self.sheety_api_iata_codes}")