# store the locations in a list. Make sure the list is not in alphabetical order
countries = ["Spain", "USA", "Norway", "Australia", "New Zealand"]

# print list in it's original order
print("1. " + str(countries))

# use sorted() to print your list in alphavetical order whitout modifying the acttual list
print("2. " + str(sorted(countries)))

# show that your list is stil in it's original order
print("3. " + str(countries))

# use sorted() to print your list in reverse alphabetical order without changing the order of the original list
print("4. " + str(sorted(countries, reverse = True)))

# show that your list is stil in it's original order
print("5. " + str(countries))

# use reverse() to change the order of your list
countries.reverse()
print("6. " + str(countries))

# use revers() to change the order of your list again
# use reverse() to change the order of your list
countries.reverse()
print("7. " + str(countries))

# sort the list in alphabetically using sort()
countries.sort(reverse=True)
print("8. " + str(countries))
