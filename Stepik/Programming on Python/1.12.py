# ex. => 1.12.1
# find the area of a triangle using Heron's formula
side1 = int(input())
side2 = int(input())
side3 = int(input())

# semi-perimeter
p = (side1 + side2 + side3)/2

S = (p*(p-side1)*(p-side2)*(p-side3)) ** 0.5
print(S)



# ex. => 1.12.2
# Does this number fall in this interval?
num = int(input())
if -15 < num <= 12 or 14 < num < 17 or num >= 19:
    print(True)
else:
    print(False)



# ex. => 1.12.3
# simple kalkulator
first_num = float(input())
second_num = float(input())
operation = input()
if operation == "+":
    print(first_num + second_num)
elif operation == "-":
    print(first_num - second_num)
elif operation == "*":
    print(first_num * second_num)
elif operation == "/":
    if second_num == 0:
        print("Деление на 0!")
    else:
        print(first_num / second_num)
elif operation == "mod":
    if second_num == 0:
        print("Деление на 0!")
    else:
        print(first_num % second_num)
elif operation == "pow":
    print(first_num ** second_num)
elif operation == "div":
    if second_num == 0:
        print("Деление на 0!")
    else:
        print(first_num // second_num)



# ex. => 1.12.4
# find the area of the figure
geometric_figure = input()
if geometric_figure == "triangle":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(float(S))
elif geometric_figure == "rectangle":
    a = int(input())
    b = int(input())
    S = a * b
    print(float(S))
elif geometric_figure == "circle":
    r = int(input())
    S = 3.14 * (r**2)
    print(float(S))

# ex. => 1.12.5
# print three lines to the console: first the maximum, then the minimum, after which the remaining number.
first_num = int(input())
second_num = int(input())
third_num = int(input())
numbers = [first_num, second_num, third_num]
SUM = sum(numbers)
print(max(numbers))
print(min(numbers))
print(SUM - max(numbers) - min(numbers))



# ex. => 1.12.6
num = input()
if num[-1] == "1" and num[-2:] != "11":
    print(f"{num} программист")
elif num[-1] in ["2", "3", "4"] and num[-2:] not in ["12", "13", "14"]:
    print(f"{num} программиста")
else:
    print(f"{num} программистов")



# ex. => 1.12.7 => happy ticket
# if sum of the firsts numbers and sum of the last three numbers are match, print => happy ticket
number = int(input())
if sum(map(int, number[:3])) == sum(map(int, number[3:])):
    print("Happy ticket")
else:
    print("Regular ticket")

