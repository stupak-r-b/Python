# store the numbers 1 through 9 in a list
numbers = [number for number in range(1, 10)]

# loop through the list. You output should read "1st, 2nd, 3rd, 4th"
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
