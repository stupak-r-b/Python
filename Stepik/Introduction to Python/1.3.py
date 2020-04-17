# ex. 1.3.2
# write a program that takes two integers and prints their sum
first_num = int(input())
second_num = int(input())
SUM = sum(first_num, second_num)
print(f"{SUM}")



# ex. 1.3.3
# write a program that calculates the area of an arbitrary rectangle from two
# entered numbers - the lengths of its sides
first_num = float(input())
second_num = float(input())
area = first_num * second_num
print(f"{area}")



# ex. 1.3.5
# write a program that calculates the kinetic energy of the body
mass = float(input())
speed = float(input())
print(f"{(mass * speed**2)/2}")