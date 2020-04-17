# write a function that accepts the name of a city and its country
def describe_city(city, country="Spain"):
    print(f"{city} is in {country}")

# call function for three different cities
describe_city("Madrid")
describe_city("Valencia")
describe_city(city="Porto", country="Portugal")