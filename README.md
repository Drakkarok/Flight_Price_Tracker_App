# Flight_Price_Tracker_App  

Short description:  
An app that searches for the price of flights on predefined routes  with predefined maximum price tags and sends an email with all destionations found.  

Long description:  
1. Takes a CSV file in the form of a Google Sheets doc from drive using SMTP Port (sheet 1).  
   Note: Header of the CSV: City, Country, IATA Code, Highest Price.  
   Note: "City" and "Highest Price" are mandatory parameters to be filled in the sheet  
2. It takes a look at the IATA codes inside the data. For every city that does not have a IATA code it makes a search using Tequila by Kiwi API for finding the missing ones.  
3. With the IATA codes filled, it makes a flight search for the next 6 months from a depature city (customizable) to an arrival city (provided by the IATA codes) with respect to the Highest Price parameter taken from sheet 1.  
   Note: There are customizable parameters for the flight search such as:  
   a) Type of currency ("curr" parameter) - default RON;  
   b) Flight type ("flight_type" parameter) - default round;  
   c) Number of adults ("adults" parameter) - default 2;  
   d) Minimum number of nights stayed ("nights_in_dst_from" parameter) - default 7;  
   e) Maximum number of nights stayed ("nights_in_dst_to" parameter) - default 28;  
4. Based on the findings it makes a list of available cities to fly to.  
5. Takes a CSV file in the form of a Goggle Sheets doc from drive using SMTP Port (sheet 2).  
   Note: Header of the CSV: First Name, Last Name, Email.  
6. Sends a customized email to every email address with the destionations available.  

---

## CONFIGURATION  

### SMTP Port  
Please follow the "CONFIGURATION - SMTP Port" presented in "Birthday_Congratulation_Autosender" for configuring the SMTP Port.  
Link: [https://github.com/Drakkarok/Birthday_Congratulation_Autosender/blob/main/README.md](url)  
After following the linked document please replace "self.email_to_send_from" and "self.password_for_email" with your own email and app password in NotificationManager (Class).  

### Google Sheets  
1. You will need to create a new Google Sheets document inside your drive.  
2. It should contain two sheets ("sheet1" and "sheet2");  
3. On the first sheet ("sheet1") the first line should contain City, Country, IATA Code, Highest Price. Every parameter should be contained in a separate cell and without any commas;  
4. Be sure to fill some data inside the sheet (mandatory parameters: City, Highest Price);  
5. The first line in the second sheet ("sheet2") should contain First Name, Last Name, Email. Every parameter should be contained in a separate cell and without any commas;  
6. Be sure to fill all the data inside the sheet (mandatory parameters: First Name, Last Name, Email).  

### Tequila by Kiwi API - key  
You will need an Tequila by Kiwi account (free version) in order to get your "self.tequila_api_token" in DataManager (Class). Simply replace it in the code.  
Link: [https://tequila.kiwi.com/portal/getting-started](url)  

### Sheety API - key  
You will need a Sheety API account (free version) in order to get your "self.sheety_api_token" and the links to your Google Sheets endpoints.  
Link: [https://sheety.co/](url)  
Follow the steps:  
1. After creating your Sheety API account go to Dashboard;  
2. Click on create New Project;  
3. Click on From Google Sheet;  
4. Copy and paste your google sheet URL;  
5. Write the Project Name;  
6. Click on create;  
7. Enter in your newly created project;  
8. Go to Authentification;  
9. Select Bearer (Token);  
10. Copy and paste the Token inside the code (self.sheety_api_token parameter inside DataManager (Class));  
11. Go to API and click sheet1. Be sure "GET" is enabled;  
12. Copy and paste the link inside the code (self.sheety_api_endpoint_get parameter inside DataManager (Class));  
13. Click on sheet2. Be sure "GET" is enabled;  
14. Copy and paste the link inside the code (self.sheety_api inside NotificationManger (Class)).  

---

Build using: 
- requests;
- datetime;
- smtplib.

Functions:
- N/A.

Classes:
- (1) DataManager;
- (2) FlightSearch;
- (3) NotificationManager.

Methods:
- (1) request_data_get;
- (1) request_iata_codes;
- (1) print;
- (2) make_a_search;
- (2) available_cities;
- (3) download_emails;
- (3) send_email_to.
