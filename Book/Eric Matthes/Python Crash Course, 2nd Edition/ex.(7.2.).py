# write a program that asks the user how many people are in their dinner group
places = input("How many seats do you want to book a table in a restaurant?: ")
if int(places) > 8:
    print("Excuse me but you need wait.")
else:
    print("The table is ready.")
