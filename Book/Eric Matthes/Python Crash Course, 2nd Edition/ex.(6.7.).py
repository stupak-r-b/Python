peoples = [{"first_name": "Alex", "last_name": "Peterson", "city": "New York"},
          {"first_name": "Mike", "last_name": "Miller", "city": "Oklahoma"},
          {"first_name": "Bob", "last_name": "Foster", "city": "Miami"}]

# used a loop to print keys and values from dictionaries from a list
print("\nThe list of person i knew: ")
for person in peoples:
    # used generator and added keys to the list
    keys = [key for key in person.keys()]

    # used keys and printed values
    print(f"- {person[keys[0]]} {person[keys[1]]} from {person[keys[2]]}")
