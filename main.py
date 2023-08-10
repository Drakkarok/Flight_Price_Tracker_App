from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
tequila_api_key = "dToFYwj1f0sjm_aRczoLJm7yCNBehX5C"


data_manager_api = DataManager()
flight_search_manager = FlightSearch(data_manager_api)
notification_manager = NotificationManager(flight_search_manager)
