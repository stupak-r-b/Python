# use a dictionary to store people's favorite numbers
numbers = {"Alex": 3, "Viktoriia": 7, "Peter": 21, "Matha": 13, "Ben": 4}
keys = numbers.keys()

# print each person's name and their favorite number
for key in keys:
    print(f"{key}'s favorite number is {numbers[key]}.")
