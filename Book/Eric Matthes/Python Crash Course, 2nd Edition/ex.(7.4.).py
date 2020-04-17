# write a loop that prompts the user to enter a series of pizza toppings until they enter a "quit" value
while True:
    topping = []
    print("\n*print 'quit' to exit.\n")
    order = input("What toppings would you like to add to pizza?: ")
    if order == "quit":
        break
    print(f"You'll add that topping to pizza.")
