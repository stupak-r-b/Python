# favorite numbers
numbers = {"Alex": [3, 4], "Viktoriia": [7, 9, 3], "Peter": [21, 13, 7], "Matha": [8, 9, 10], "Ben": [1, 2, 3, 4]}
keys = numbers.keys()

# use the key, print their values
for key in keys:
    favorite = "".join(str(num) + ", " for num in numbers[key] if num != numbers[key][-1])
    print(f"{key}'s favorite number is {favorite}and {numbers[key][-1]}.")
