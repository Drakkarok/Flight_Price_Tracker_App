import requests
from data_manager import DataManager
import datetime


class FlightSearch:
    def __init__(self, data_manager_api: DataManager):
        self.data_manager_api = data_manager_api
        self.test = self.data_manager_api.tequila_api_token
        self.date_today_unformatted = datetime.datetime.today()
        self.date_tomorrow_unformatted = self.date_today_unformatted + datetime.timedelta(days=1)
        self.date_tomorrow = f"{self.date_tomorrow_unformatted.strftime('%d')}/" \
                             f"{self.date_tomorrow_unformatted.strftime('%m')}/"\
                             f"{self.date_tomorrow_unformatted.strftime('%Y')}"
        self.date_in_six_months_unformatted = self.date_today_unformatted + datetime.timedelta(days=6 * 30)
        self.date_in_six_months = f"{self.date_in_six_months_unformatted.strftime('%d')}/" \
                                  f"{self.date_in_six_months_unformatted.strftime('%m')}/" \
                                  f"{self.date_in_six_months_unformatted.strftime('%Y')}"
        self.search_result = []
        self.list_of_available_cities = []
        self.make_a_search()

    def make_a_search(self):
        for index, city_iata_code in enumerate(self.data_manager_api.sheety_api_iata_codes):
            parameters = {
                "fly_from": "LHR",
                "fly_to": f"{city_iata_code}",
                "date_from": f"{self.date_tomorrow}",
                "date_to": f"{self.date_in_six_months}",
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "adults": 2,
                "curr": 'RON',
                "price_to": self.data_manager_api.sheety_api_result["sheet1"][index]["highestPrice"]*50,
                "max_stopovers": 0
                }
            response = requests.get(url="https://api.tequila.kiwi.com/v2/search",
                                    params=parameters,
                                    headers=self.data_manager_api.tequila_api_header)
            response.raise_for_status()
            result = response.json()
            print(result)
            for i in range(0, len(result["data"])-1):
                self.search_result.append({
                        "iata_code": city_iata_code,
                        "departure_date_in": result["data"][i]["route"][0]["utc_departure"],
                        "departure_date_from": result["data"][i]["route"][1]["utc_departure"],
                        "price": result["data"][i]["price"],
                    }
                    )
        self.available_cities()

    def available_cities(self):
        set_of_available_cities = set()
        for dictionary in self.search_result:
            set_of_available_cities.add(dictionary["iata_code"])
        self.list_of_available_cities = list(set_of_available_cities)
        print(f"Those are the available cities to fly to: {self.list_of_available_cities}")