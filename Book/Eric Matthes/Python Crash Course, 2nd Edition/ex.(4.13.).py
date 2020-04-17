# create a tuple of 5 elements
menue = ("Caril de Frango", "Karahi Chicken", "Chicken Jalfrezi",
         "Chicken Vindaloo", "Chicken Xacuti")

# use a for loop to print each food the restaurant offers
print("Dishes from the menu: ")
for dish in menue:
    print(f"- {dish}")

# try to modify one of the items, and make sure that Python rejects the change
#menue[0] = "Mango Chicken"

# add a block of code that rewrites the ruple
new_menue = ("Mango Chicken", "Chicken Curry") + menue[2:]

print("\nDishes from the new menu: ")
for dish in new_menue:
    print(f"- {dish}")
