from flight_search import FlightSearch
import requests
import smtplib


class NotificationManager:
    def __init__(self, flight_search_manager: FlightSearch):
        self.flight_search_manager = flight_search_manager
        self.email_to_send_from = "dummy@Gmail.com"
        self.password_for_email = "password"
        self.email_dict = {}
        self.sheety_api = "address"
        self.download_emails()

    def download_emails(self):
        response = requests.get(url=self.sheety_api, headers=self.flight_search_manager.data_manager_api.sheety_api_header)
        response.raise_for_status()
        self.email_dict = response.json()
        self.send_email_to()

    def send_email_to(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(self.email_to_send_from, self.password_for_email)
            for entity in self.email_dict["sheet2"]:
                if len(self.flight_search_manager.list_of_available_cities) == 0:
                    message = f"Subject:Hello {entity['firstName']} {entity['lastName']}! Sadly, no flights are available :(\n\n" \
                              f"I apologize for the inconvenience, but I couldn't find any flights that match your " \
                              f"required description. I appreciate your understanding."
                else:
                    message = f"Subject: Hello! Good news, we found some flights for your preferred destinations! \n\n"\
                              f"Greetings {entity['firstName']} {entity['lastName']}! We found flights to the " \
                              f"following destinations {self.flight_search_manager.list_of_available_cities}"
                message_encoded = message.encode('utf-8')
                connection.sendmail(from_addr=self.email_to_send_from,
                                    to_addrs=entity["email"],
                                    msg=message_encoded)

