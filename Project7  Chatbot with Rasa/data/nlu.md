## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hola
- Hi

## intent:deny
- no
- not required
- [Nope](deny)

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [Mexican](cuisine)
- Hi there! I'm looking for a [mexican](cuisine) restaurant in [Bangaluru]{"entity": "location", "value": "bangalore"}
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "medium"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- I want to eat something [expensive]{"entity": "price", "value": "high"}
- Please find me some [moderately](price) priced restaurants
- How about in [mumbai](location)
- [Less than 300](price)
- my budget is [lesser than Rs. 300]{"entity": "price", "value": "low"}
- my budget is [More than Rs. 700]{"entity": "price", "value": "high"}
- my budget is [between Rs. 300 to 700]{"entity": "price", "value": "medium"}
- [300-700](price) range
- show me the [costliest](price) restaurants
- I need a restaurant in [Pathanamthitta](location)
- I need to find a restaurant in [Pathanamthitta](location)
- I need to find a restaurant at [Rishikesh](location)
- I need to find a [Mexican](cuisine) restaurant
- I need to find a restaurant at [Allahabad](location)
- Need to find a good restaurant in [Mumbai](location)
- Find a [Chinese]{"entity": "cuisine", "value": "chinese"} restaurant
- Find a [Chinese]{"entity": "cuisine", "value": "chinese"} Restaurant in [Mumbai](location)
- Find me a restaurant in [Mumbai](location)
- [More than Rs. 700]{"entity": "price", "value": "high"}
- Need to find a restaurant at [Ludhiana](location)
- [between Rs. 300 to 700]{"entity": "price", "value": "medium"}
- Find me a restaurant in [Ratnagiri](location)
- Find me a [chinese](cuisine) restaurant
- [Mumbai](location)
- [More than Rs. 700]{"entity": "price", "value": "high"}

## intent:give_email
- [abc123@gmail.com](email)
- yes. please send it to [abc123@gmail.com](email)
- my email is [abc123@gmail.com](email)
- [reachanish1512@gmail.com](email)
- [abc@gmail.com](email)

## synonym:4
- four

## synonym:Ajmer
- Ajmr

## synonym:America
- american
- america
- pizza
- burger

## synonym:Delhi
- New Delhi
- delhi

## synonym:Italian
- italic
- italia

## synonym:Kolkata
- calcutta

## synonym:Mumbai
- bombay

## synonym:Pune
- Poona

## synonym:bangalore
- Bangaluru
- Bengaluru
- blr

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:high
- expensive
- More than Rs. 700
- more than Rs. 700
- morethan 700
- more than 700
- above 700
- costliest
- >700
- 700 or more

## synonym:low
- lesser than Rs. 300
- Lesser than Rs. 300
- lessthan 300
- less than 300
- below 300
- 300 or below
- pocket-friendly
- <300
- cheap
- cheaper
- inexpensive

## synonym:medium
- moderate
- between Rs. 300 to 700
- Rs. 300 to 700
- between Rs. 300 and 700
- 300 to 700
- 300-700
- budget
- moderately

## synonym:vegetarian
- veggie
- vegg

## regex:email
- [a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.][a-zA-Z]+[.]{0,1}[a-zA-Z]{0,2}$

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}
