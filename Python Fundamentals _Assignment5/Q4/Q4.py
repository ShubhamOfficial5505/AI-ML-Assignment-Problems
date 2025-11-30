''' In Python, only functions, classes, and modules create new scopes.
    Statements like if, for, while, with, and try/except do NOT.
    Anything defined inside them live in the same scope as the
    surrounding block '''

# The order in which python evaluates names is LEGB (Local → Enclosing → Global → Built-in)

import json

city_population_millions = {
    "Mumbai": 21.6,
    "Kolkata": 15.5,
    "Delhi": 33.8
}

with open("cities.json", "w") as f_write:
    json.dump(city_population_millions, f_write, indent = 4, sort_keys = True)

with open("cities.json", "r") as f_read:
    city_data = json.load(f_read) # Global Scope
    for city, population in city_data.items():
        print(f"City: {city } Population: { population }")

try:
    new_city_data = input("\nEnter city name and population: ").split()
    city_data.update({ new_city_data[0]: float(new_city_data[1]) })
except:
    print("Invalid Input")
else:
    with open("cities.json", "w") as f_update:
        json.dump(city_data, f_update, indent = 4, sort_keys = True)