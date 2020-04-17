# make a dictionary called cities. Use the names of three cities as keys in your dictionary
cities = [{"New York": {"country": "USA", "population": "8_623_000", "fact": "More than 800 languages are spken in New York City"}},
          {"Moscow": {"country": "Russia", "population": "11_920_000",
           "fact": "Moscow claims the largest number of billionaires in the world. Per Forbes, there are 84 billionaires in the city"}},
          {"Paris": {"country": "France", "population": "2_148_000", "fact": "Paris was originally a Roman City called 'Lutetia."}}]

# print the name of each city and all of the information you have stored about it
for i in cities:
    for city, info in i.items():
        print(f"\nInteresting information about {city}")
        print(f'\t- The {city} is a city in {info["country"]}.')
        print(f'\t- Population of {city} is {info["population"]}.')
        print(f'\t- Interesting fact about {city}: {info["fact"]}.')