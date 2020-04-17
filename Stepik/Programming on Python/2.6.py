# ex. => 2.6.1
# write a program that reads numbers from the console until the sum of the entered numbers is 0 and
# immediately after that displays the sum of the squares of all the numbers read
some_list = []
while True:
    number = int(input())
    some_list.append(number)
    if sum(some_list) == 0:
        some_list = [num**2 for num in some_list]
        print(sum(some_list))
        break



# ex. => 2.6.2
# write a program that outputs part of a sequence of numbers
# for example, if n = 7, then the program should print 1 2 2 3 3 3 4.
lenth = int(input())
numbers = []
for num in range(1, lenth + 1):
    for i in range(num):
        if len(numbers) != lenth:
            numbers.append(str(num))
print(" ".join(number for number in numbers))



# ex. => 2.6.3
# write a program that displays all the positions where the number of "num" appears in the transferred list "str3"
str1 = input()
num = input()
count = -1
string = ""
for item in str1.split(" "):
    if item == num:
        count += 1
        string += str(count) + " "
        continue
    count += 1
if len(string) > 0:
    print(string)
else:
    print("Отсутствует")



# ex. => 2.6.4
# the program should output a matrix of the same size for which each element on position i,j is
# equal to the sum of the matrix elements at positions (i-1, j), (i+1, j), (i, j-1), (i, j+1)
lst1 = []
new = []
while True:
    # user input
    input1 = input()
    if input1 == "end": break
    lst1.append([num for num in input1.split(" ")])
for i in range(len(lst1)):
    some_list = []
    for j in range(len(lst1[i])):
        # position (i-1, j)
        a = lst1[i-1][j]

        # position (i+1, j)
        b = lst1[0][j] if i == len(lst1)-1 else lst1[i+1][j]

        # position (i, j-1)
        c = lst1[i][j-1]

        # position (i, j+1)
        d = lst1[i][0] if j == len(lst1[i])-1 else lst1[i][j+1]

        # sum of the matrix elements at positions (i-1, j), (i + 1, j), (i, j-1), (i, j + 1)
        some_list.append(int(a) + int(b) + int(c) + int(d))
    new.append(some_list)

# information output cycle
for item in new:
    print(" ".join(str(num) for num in item))



# ex. => 2.6.5.
# print an n*n table, filled with numbers from 1 to n*2 in a spiral, coming out of the upper
# left corner and twisted clockwise
num = int(input())

# create an array of size n * n filled with zeros
n_list = [[0 for x in range(num)] for y in range(num)]
# fill the array with numbers starting from 1
start = 1
# smallest index
low = 0
# highest index
high = num
count = int((num+1)/2)

# array filling cycle
for i in range(count):
    # top edge of an array of size n * n
    for j in range(low, high):
        n_list[i][j] = start
        start += 1

    # right edge of an array of size n * n
    for j in range(low+1, high):
        n_list[j][high-1] = start
        start += 1

    # bottom edge of an array of size n * n
    for j in range(high-2, low-1, -1):
        n_list[high-1][j] = start
        start += 1

    # right edge of an array of size n * n
    for j in range(high-2, low, -1):
        n_list[j][low] = start
        start += 1

    low += 1
    high -= 1

# information output cycle
for i in range(num):
    for j in range(num):
        print(n_list[i][j], end=" ")
    print()