# recommended to sleep A hours a day
A = int(input())

# is sleeping B hours a day bad for you
B = int(input())

# user sleep H hours a day
H = int(input())

if H > B:
    print("You sleep too much")
elif H < A:
    print("You sleep too little")
else:
    print("You sleep normal amount of time")


# How do you find if a year is a leap year in Python?
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Is a leap year")
else:
    print("Is a normal year")