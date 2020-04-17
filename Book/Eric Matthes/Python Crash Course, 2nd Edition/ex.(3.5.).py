# my guests
guests = ["Sarah", "Jozeph", "Mike", "Alex", "Garry"]

# replace the name of the guest who can't make the dinner with the name of the new person you are inviting
guests[0] = guests[0].replace("Sarah", "Deny")

# use insert() to add one new guest to the beginning of your list
guests.insert(0, "Mary")

# use insert() to add one new guest to the middle of your list
guests.insert(3, "Kate")

# use append() to add one new guest to the end of your list
guests.append("Donald")

# Mike can't come tomorrow
guests.remove("Mike")

# ...and Mary can't come tomorrow
del guests[0]

# print a new set of invitation messages, one for each person in your list
for guest in guests:
    print("\n\nInvitation Messages for Dinner\n")
    print(f"Dear {guest} you are most cordially invited to be our guest at thedinner party we have arranged on 28.02")
    print("It will be great having you among us!")