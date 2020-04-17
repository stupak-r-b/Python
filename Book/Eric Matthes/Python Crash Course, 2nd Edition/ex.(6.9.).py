# make a dictionary called favorite_places
favorite_places = [{"Jessey": ["Grand Canyon", "Victoria Falls", "Angel Falls"]},
                   {"Alex": ["Atelope Canyon", "Atacma Desert", "Arashiyame Bamboo Grove"]},
                    {"Bob": ["Antarctica", "Avenue Of The Baobabs", "The Azores"]}]

# loop  through the dictionary, and print each person's name and their favorite places
for dictionary in favorite_places:
    for key, value in dictionary.items():
        places = "".join(place + ", " for place in value if place != value[-1])
        print(f"{key}'s favorite places: {places} and {value[-1]}.")