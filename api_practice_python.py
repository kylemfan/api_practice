import requests

# HTTP GET REQUEST FROM URL:
response = requests.get("https://randomuser.me/api")
print('DISCLAIMER: Every time this Python script is run, the information of a (fake) random person appears.')

# status_code = 200 if OK
# print(response.status_code)

# items variable is JSON object
items = response.json()

# Selector for name key:
name_select = items["results"][0]["name"]

# Gender & name info
gender = items["results"][0]["gender"]
title = name_select["title"]
first_name = name_select["first"]
last_name = name_select["last"]

# Formatting for full_name
abbreviated_titles = ["Mr", "Ms", "Mrs", "Dr"]
if (title in abbreviated_titles):
    full_name = f'{title}. {first_name} {last_name}'
else:
    full_name = f'{title} {first_name} {last_name}'

# Selector for location key:
location = items["results"][0]["location"]

# Address info
street_name = location["street"]["name"]
house_number = location["street"]["number"]
zip_code = location["postcode"]
full_address = f'{house_number} {street_name}, {zip_code}'

# State & country info
city_name = location["city"]
state_name = location["state"]
country_name = location["country"]
city_state_country = f'City of {city_name}, {state_name} in {country_name}'

print(full_name)