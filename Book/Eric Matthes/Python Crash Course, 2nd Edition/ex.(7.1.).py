# write a program that asks the user what kid of rental cor they would like
car = input("What your favorite car?: ")

# if user uses only letters
if car.isalpha():
    print(f"Let me see if I can find you a {car}")
    input("Press Enter to exit.")
else:
    print("Use only english alphabet. Try again")
