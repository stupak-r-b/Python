# ex. => 1.4.1
# print the length of the string
some_string = input()
print(len(some_string))



# ex. => 1.4.2
# print the maximum number
print(max([int(input()), int(input())]))



# ex. => 1.4.3
# print the minimum number
print(min([int(input()), int(input())]))



# ex. => 1.4.4
# find the area of a triangle using the Heron formula
a = float(input())
b = float(input())
c = float(input())
p = (a + b + c)/2
S = (p*(p - a)*(p - b)*(p - c))**0.5
print(S)



# ex. => 1.4.5
# calculate how many hours and minutes elapsed between times
first_num = int(input())
second_num = int(input())
result = max([first_num, second_num]) - min([first_num, second_num])
hours = result // 60
minutes = result - hours * 60
print(hours, minutes)