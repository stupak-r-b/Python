# set a value for the variable age
age = 35

# if the person is less than 2 years old, print a message that the person is a baby.
if age < 2:
    print("You're still baby.")

# if the person is at least 2 years old but less than 4, print a message that the person is a toddler
elif 2 <= age < 4:
    print("You're a toddler")

# if the person is at least 4 years old but less than 13, print a message that the person is a kid
elif 4 <= age < 13:
    print("You're still a kid.")

# if the person is at least 13 years old but less than 20, print a message that the person is a teenager
elif 13 <= age < 20:
    print("You're a teenager.")

# if the person is at least 20 years old but less than 65, print a message that the person is an adult
elif 20 <= age < 65:
    print("You are an adult.")

# if the person is age 65 or older, print a message tha the person is an elder.
else:
    print("You are an old man.")
