## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_confirm
* affirm
    - utter_ask_email_address
* give_email{"email": "abc123@gmail.com"}
    - slot{"email":"abc123@gmail.com"}
    - action_send_recomendation
    - utter_goodbye
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_confirm
* affirm
    - utter_ask_email_address
* give_email{"email": "abc123@gmail.com"}
    - slot{"email":"abc123@gmail.com"}
    - action_send_recomendation
    - utter_goodbye
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - utter_ask_budget
* restaurant_search{"price":"low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"recomend":"Found"}
    - utter_ask_email_confirm
* affirm
    - utter_ask_email_address
* give_email{"email": "abc123@gmail.com"}
    - slot{"email":"abc123@gmail.com"}
    - action_send_recomendation
    - utter_goodbye

## happy_path_no_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - utter_ask_budget
* restaurant_search{"price":"low"}
    - slot{"price":"low"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"recomend":"Found"}
    - utter_ask_email_confirm
* deny
    - utter_goodbye


## Invalid city path_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Pathanamthitta"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Pathanamthitta"}
    - utter_invalid_city
    - utter_goodbye


* greet
    - utter_greet
* restaurant_search{"location": "Pathanamthitta"}
    - slot{"location": "Pathanamthitta"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - utter_invalid_city
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"location": "Pathanamthitta"}
    - slot{"location": "Pathanamthitta"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - utter_invalid_city
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - utter_invalid_city
    - utter_goodbye

* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_invalid_city
    - utter_goodbye

* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"recomend": "Mystery Box in Shop 2 & 3, Pleasant Park, Opposite Movie Time Theatre, Kachpada Signal, Evershine Nagar, Malad West, Mumbai has been rated 4.2\nAverage Cost for two :550\n\nUncle's Kitchen in Sunder Lane, Off Link Road, Orlem, Malad West, Mumbai has been rated 4.1\nAverage Cost for two :500\n\nThe Darjeeling in B-41, Unit 2, Boolani Estate Owner’s Premises, Co-op Society, New Link Road, Opposite Citi Mall, Veera Desai Area, Mumbai has been rated 4.1\nAverage Cost for two :600\n\nThotrin Cafe in Shop 2, Kolivery Village, Opposite St. Roque, Kalina, Santacruz East, Mumbai has been rated 4.1\nAverage Cost for two :500\n\nCantonese in Shop 10, Ratnamani Society, Dada Patilwadi, Naupada, Thane West, Thane has been rated 4.1\nAverage Cost for two :550\n\nDimsum (Momo) Express in Shop 4, Cecelia Sagar, Wireless Road, Bamanpuri, Ekta Nagar, Chakala, Mumbai has been rated 4.0\nAverage Cost for two :500\n\nZoodles - Oriental Street Wok in Ground Floor, Shalimar Morya Park, Off New Link Road, Opposite Infinity Mall, Oshiwara, Andheri West, Mumbai has been rated 4.0\nAverage Cost for two :600\n\nSilli Chilli in 311, Snehanjali CHS, Near Samarth Aishwarya Building, Adarsh Nagar, Andheri Lokhandwala, Andheri West, Mumbai has been rated 3.9\nAverage Cost for two :400\n\nKung Fu Panda in Ground Floor, Indi Saigon Industrial Estate, Marol, Mumbai has been rated 3.9\nAverage Cost for two :600\n\nDimsum (Momo) Express in Shop 24, 170/A, Baxu Bhai Mansion, SV Road, Near Talav Signal, Nr. Sai Sagar Hotel, Hill Road, Bandra West, Mumbai has been rated 3.8\nAverage Cost for two :500\n\n"}
    - utter_ask_email_confirm
    - utter_ask_email_address
* give_email{"email": "reachanish1512@gmail.com"}
    - slot{"email": "reachanish1512@gmail.com"}
    - action_send_recomendation
    - utter_goodbye

* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"recomend": "Mirchi And Mime in G6,One Boulevard,Lake Boulevard Road, Hiranandani Business Park, Powai, Mumbai has been rated 4.9\nAverage Cost for two :1800\n\nBastian in B/1, New Kamal Building, Opposite National College, Linking Road, Bandra West, Mumbai has been rated 4.8\nAverage Cost for two :4200\n\nMasala Library in Ground Floor, First International Financial Centre, Bandra Kurla Complex, Mumbai has been rated 4.8\nAverage Cost for two :3500\n\nAer - Four Seasons in 1/136, E Moses Road, Worli, Mumbai has been rated 4.7\nAverage Cost for two :4500\n\nHakkasan in 206, 2nd Floor, Krystal, Waterfield Road, Linking Road, Bandra West, Mumbai has been rated 4.7\nAverage Cost for two :2600\n\nBombay Salad Co. in Shop 1, 16th Road, Linking Road, Bandra West, Mumbai has been rated 4.7\nAverage Cost for two :900\n\nGallops in Mahalaxmi Race Course, Mahalaxmi, Mumbai has been rated 4.6\nAverage Cost for two :2600\n\nThe Fusion Kitchen in Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC Colony, Borivali West, Mumbai has been rated 4.6\nAverage Cost for two :1600\n\nSammy Sosa in Shop 18, Meera CHS, Near Mega Mall, Oshiwara Link Road, Oshiwara, Andheri West has been rated 4.6\nAverage Cost for two :1600\n\nBurma  Burma in Kothari House, Allana Centre Lane, MG Road, Near Mumbai University, Fort, Mumbai has been rated 4.6\nAverage Cost for two :1600\n\n"}
    - utter_ask_email_confirm
* deny{"deny": "Nope"}
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"location": "Ludhiana"}
    - slot{"location": "Ludhiana"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - utter_ask_email_confirm
* deny{"deny": "Nope"}
    - utter_goodbye

* restaurant_search{"location": "Ratnagiri"}
    - slot{"location": "Ratnagiri"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_invalid_city
    - utter_goodbye

* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_budget
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email_confirm
* give_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_recomendation
    - utter_goodbye
