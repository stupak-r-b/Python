# ex. => 1.5.1
# write a program that prints "even" if the entered integer is even, and "odd" otherwise
number = int(input())
if number % 2 == 0:
    print("even")
else:
    print("odd")



# ex. => 1.5.2
# maximum and minimum without any function
first_num = int(input())
second_num = int(input())
if first_num > second_num:
    print(f"A larger number: {first_num}, lower number: {second_num}")
else:
    print(f"A larger number: {second_num}, lower number: {first_num}")



# ex. => 1.5.3
# Determine if the number is large. If the number is more than a billion write "Yes"
number = int(input())
if abs(number) > 1_000_000_000:
    print("Yes")
else:
    print("No")



# ex. => 1.5.4
# Two arithmetic operations. Add or Subtract
first_number = float(input())
second_number = float(input())
operation = input()
if operation == "+":
    print(f"{first_number + second_number}")
else:
    print(f"{first_number - second_number}")



# ex. => 1.5.5
# You need to analyze the entered number 0 <= n < 1000, and display "one-digit number", "two-digit number"
# or "three-digit number" depending on the length of the number
number = input()
if len(number) == 1:
    print("One-digit number")
elif len(number) == 2:
    print("Two-digit number")
else:
    print("Three-digit number")