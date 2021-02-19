from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from abc import ABC

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

service_cities = ["Ahmedabad", "Bengaluru", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai", "Pune"]


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "f4924dc9ad672ee8c4f8c84743301af5"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)

        cities = ['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune',
                  'Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly',
                  'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bokaro Steel City',
                  'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Dhanbad', 'Durg-Bhilai Nagar', 'Durgapur',
                  'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gurgaon',
                  'Guwahati', 'Gwalior', 'Hubli-Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu',
                  'Jamnagar',
                  'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kannur', 'Kanpur', 'Kakinada', 'Kochi', 'Kottayam', 'Kolhapur',
                  'Kollam',
                  'Kota', 'Kozhikode', 'Kurnool', 'Lucknow', 'Ludhiana', 'Madurai', 'Malappuram', 'Mathura', 'Goa',
                  'Mangalore',
                  'Meerut', 'Moradabad', 'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Palakkad',
                  'Patna',
                  'Pondicherry', 'Prayagraj', 'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem',
                  'Sangli',
                  'Siliguri', 'Solapur', 'Srinagar', 'Sultanpur', 'Surat', 'Thiruvananthapuram', 'Thrissur',
                  'Tiruchirappalli',
                  'Tirunelveli', 'Tiruppur', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City',
                  'Vijayawada']
        cities_lower = [x.lower() for x in cities]

        if loc.lower() not in cities_lower:
            dispatcher.utter_message(":'(")
            return

        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'bakery': 5, 'chinese': 25, 'cafe': 30, 'italian': 55, 'biryani': 7, 'north indian': 100,
                         'south indian': 85}

        # Zomato only sends 20 restaurants at a time if the limit is  > 20,so the api is called three times with
        # different offsets to get more than 20 Also another parameter start has been added "start" to
        # restaurant_search in zomatopy.py

        res_offset = [0, 20, 40, 60]
        restaurants = []
        for i in res_offset:
            results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20, i)
            d = json.loads(results)
            restaurants.extend(d["restaurants"])

        response = ""
        mailBody = ""
        restaurants.sort(key=lambda x: x['restaurant']["user_rating"]["aggregate_rating"], reverse=True)
        budget_res = []
        budget = tracker.get_slot('price')
        if budget == "low":
            budget_res = [x for x in restaurants if int(x['restaurant']["average_cost_for_two"]) <= 300]
        elif budget == "high":
            budget_res = [x for x in restaurants if int(x['restaurant']["average_cost_for_two"]) >= 700]
        else:
            budget_res = [x for x in restaurants if x['restaurant']["average_cost_for_two"] >= 300 and x['restaurant'][
                "average_cost_for_two"] < 700]

        if budget_res == 0:
            response = "no results"
            mailBody = "no results"
        else:
            top10 = budget_res[0:10]
            for restaurant in top10[0:5]:
                response = response + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location'][
                    'address'] + " has been rated " + restaurant['restaurant']["user_rating"]["aggregate_rating"] + "\n"
                response = response + "Average Cost for two :" + str(
                    restaurant['restaurant']["average_cost_for_two"]) + "\n\n"

            for restaurant in top10[0:10]:
                mailBody = mailBody + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location'][
                    'address'] + " has been rated " + restaurant['restaurant']["user_rating"]["aggregate_rating"] + "\n"
                mailBody = mailBody + "Average Cost for two :" + str(
                    restaurant['restaurant']["average_cost_for_two"]) + "\n\n"

        dispatcher.utter_message("-----" + response)

        return [SlotSet('location', loc), SlotSet('recomend', mailBody)]


class ActionSendRecomendation(Action):

    def name(self):
        return "action_send_recomendation"

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        recommendations = tracker.get_slot('recomend')
        mainContent = recommendations + "\n\n" + "Bon Appetit"

        # The mail addresses and password
        sender_address = 'foodiebot70@gmail.com'
        sender_pass = 'helloThere123'
        receiver_address = tracker.get_slot('email')

        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = "Here are the recommendations of " + cuisine + " cuisine in " + loc  # The subject line

        # The body and the attachments for the mail
        message.attach(MIMEText(mainContent, 'plain'))

        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
