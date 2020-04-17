# write a loop in which you ask users their age, and then tell them the cost of their mobei ticket
while True:
    age = int(input("Please tell me your age: "))
    costs = 0
    if age < 3:
        print("Your ticket is free.")
        break
    elif 3 <= age < 12:
        costs = 10
        print(f"Your ticket costs {costs}$")
        break
    else:
        costs = 15
        print(f"Your ticket costs {costs}$")
        break