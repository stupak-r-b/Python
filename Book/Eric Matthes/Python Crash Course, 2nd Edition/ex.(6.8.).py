# make several dictionaries, where the name of each dictionary is the name of pet
pets = [{"pet_name": "Teddy","kind_of_animal": "dog", "owner's_name": "Mike"},
        {"pet_name": "Daisy","kind_of_animal": "dog", "owner's_name": "Steven"},
        {"pet_name": "Max","kind_of_animal": "cat", "owner's_name": "Sara"}]

# loop through list and print everything you know about each pet
print("\nThe list of person i knew: ")
for pet in pets:

# use generator and add key to the list
    keys = [key for key in pet.keys()]

# use key and print value
    print(f"- {pet[keys[0]]} is a {pet[keys[1]]} and owner of this {pet[keys[1]]} is {pet[keys[2]]}")
