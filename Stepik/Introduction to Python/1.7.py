# ex. => 1.7.1
# write a program that displays a tuple containing numbers in the half-interval [a;b)
# if a < b, and [b; a) if b < a
first_num = int(input())
second_num = int(input())
if first_num < second_num:
    some_tuple = tuple(num for num in range(first_num, second_num))
else:
    some_tuple = tuple(num for num in range(second_num, first_num))
print(some_tuple)



# ex. => 1.7.2
# print all the even numbers on the segment [a; a*10]
num = int(input())
some_tuple = tuple(num for num in range(num, num*10+1) if num % 2 == 0)
print(some_tuple)



# ex. => 1.7.3
# print a decreading sequence of numbers, one number per line
num1 = int(input())
num2 = int(input())
if num1 > num2:
    for num in range(num1, num2, -1):
        print(num)
else:
    for num in range(num2, num1, -1):
        print(num)



# ex. => 1.7.4
# print the numbers on the half-interval [a; b) or [b; a) which are even and give a remainder of 1 when divided by 7
nums = sorted([int(input()), int(input())])
for num in range(nums[0], nums[1]):
    if num % 2 == 0 and num % 7 == 1:
        print(num)



# ex. => 1.7.5
# calculate the sum of all the numbers on the half-interval
nums = sorted([int(input()), int(input())])
some_list = [num for num in range(nums[0], nums[1])]
print(sum(some_list))



# ex. => 1.7.6
# count the factorial of a number
factorial = 1
for num in range(1, int(input())+1): factorial *= num
print(factorial)



# ex. => 1.7.7
# write a program that takes a natural number n as an input and prints the first n colors of the rainbow with a capital letter
rainbow = ["Красный", "Оранжевый", "Желтый", "Зеленый", "Голубой", "Синий", "Фиолетовый"]
num = int(input())
if num > 7:
    print("Радуга состоит только из семи цветов")
else:
    for colour in rainbow[:num]:
        print(colour)



# ex. => 1.7.8
# input format: on the first line a natural number is entered - the amount of money, on the second
# line - the number of goods n, on the next n lines - the price of each of the goods
my_money = int(input())
shopping_list = int(input())
my_goods = []
for good in range(shopping_list):
    my_goods.append(int(input()))

if sum(my_goods) > my_money:
    print("Does not buy")
else:
    print("Buys")



# ex. => 1.7.9
# count the sum of the squares of all the numbers in the half-interval [a,b) or [b, a) and display it on the screen
nums = sorted([int(input()), int(input())])
nums = [num**2 for num in range(nums[0], nums[1])]
print(sum(nums))



# ex. => 1.7.10
# write a program that prints the names of months to month n
count = ["Первый", "Второй", "Третий", "Четвертый", "Пятый", "Шестой", "Седьмой", "Восьмой", "Девятый", "Десятый", "Одинадцатый", "Двенадцатый"]
months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
num = int(input())
if num > 12:
    print("Error")
else:
    for i in range(num):
        print(f"{count[i]} месяц - {months[i]}")



# ex. => 1.7.11
# Fibonacci numbers
num = int(input())
fib = [1, 1]
if num == 1: print("1")
elif num == 2: print("1 1")
else:
    while len(fib) != num: fib.append(fib[-2] + fib[-1])
    for num in fib: print(num, end=" ")



# ex. => 1.7.12
# prime or compound
num = int(input())
some_list = [i for i in range(1, num + 1)]
some_numbers = []
for i in some_list:
    if num % i == 0: some_numbers.append(i)
if len(some_numbers) == 2:
    print("Простое")
else:
    print("Составное")



# ex. => 1.7.13
# multiplication table
num = int(input())
for i in range(1, num+1):
    for j in range(i, num*i+1, i):
        print(j, end="\t")
    print()
