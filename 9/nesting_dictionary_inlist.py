'''

travel_log={
    "France":["Paris","Lille"],
    "USA":["LA","NY","FL","TX"],
    "cities_visited":["Paris","Lille"],
}
#nested visited:["Paris","Lille"],

#Nesting Dictionary in a Dictionary
travel_log={
    "France":{"cities_visited":["Paris","Lille"],"total_visits":5},
    "USA":{"cities_visited":["LA","NY","FL","TX"],"total_visits":9}
}

travel_log={
    "France":{"cities_visited":["Paris","Lille"]},
    "USA":["LA","NY","FL","TX"],
    "cities_visited":["Paris","Lille"],
}

#Nesting Dictionary in a List

travel_log=[
    {
    "country":"France",
    "cities_visited":["Paris","Lille"],
    "total_visits":5
    },
    {
    "country":"USA",
    "cities_visited":["LA","NY","FL","TX"],
    "total_visits":9
    },
]
'''


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country,visits,cities):
    new_country={}
    new_country["country"]=country
    new_country["visits"]=visits
    new_country["cities"]=cities
    travel_log.append(new_country)

add_new_country("Russia", 2, "Moscow")
print(travel_log)