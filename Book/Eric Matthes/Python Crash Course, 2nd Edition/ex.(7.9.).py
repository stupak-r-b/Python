sandwich_orders = ["egg sandwich", "pastrami", "fish sandwich", "fried egg sandwich", "pastrami", "grilled cheese sandwich"
                   "grilled chicken sandwiches", "ham sandwich", "pastrami", "ice cream sandwich"]

# use a while loop to remove all occurrences of 'pastrami' from sandwich_orders
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)

# without a loop
sandwich_orders = ["egg sandwich", "pastrami", "fish sandwich", "fried egg sandwich", "pastrami", "grilled cheese sandwich"
                   "grilled chicken sandwiches", "ham sandwich", "pastrami", "ice cream sandwich"]

sandwich_orders = [sandwich for sandwich in sandwich_orders if sandwich != "pastrami"]
print(sandwich_orders)