# ask the user for a number, and then report whether the number is a multiple of 10 or not
number = input("Type a number: ")
if int(number) % 10 == 0:
    print("Your number is a multiple of 10")
else:
    print("You number is not a multiple of 10")
