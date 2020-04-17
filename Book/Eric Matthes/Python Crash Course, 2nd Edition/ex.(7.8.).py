# make a list called sandwich_orders and fill it with the names of various sandwiches
sandwich_orders = ["egg sandwich", "fish sandwich", "fried egg sandwich", "grilled cheese sandwich"
                   "grilled chicken sandwiches", "ham sandwich", "ice cream sandwich"]
finished_sandwiches = []

# loop through the list of sandwich orders and print a message for each order
while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order}.")
    finished_sandwiches.append(order)
