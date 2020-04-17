pizzas = ["Pizza with black olives and pepperoni",
          "Pizza with capers and pecorino sardo",
          "Cauliflower crust pizza with pest and tomatoes"]

# make a copy of the list of pizzas
friend_pizzas = pizzas[:]

# add new pizza to the original list
pizzas.append("Pizza with pepperoni and pecorino sardo")

# add new pizza to the list friend_pizzas
friend_pizzas.append("Pizza with sweet and hot peppers")

# prove that you have two separate lists
print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
