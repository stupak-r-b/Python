# ex. => 2.4.1
# the numbers a and b entered from the keyboard, b > a. find the sum of factorials of numbers from the range[a; b]
[a, b] = int(input()), int(input())
def factorial(n):
    factorials = []
    for num in range(n[0], n[1]+1):
        count = 1
        for i in range(1, num+1):
            count *= i
        factorials.append(count)
    return sum(factorials)

print(factorial([a,b]))




# ex. => 2.4.2
# print the sum of the nth fibonacci number and its factorial
num = int(input())
def factorial(n):
    count = 1
    for i in range(1, num+1):
        count *= i
    return count

def fib(n):
    fib_num = [1, 1]
    count = 0
    while len(fib_num) != n:
        fib_num.append(fib_num[0+count]+fib_num[1+count])
        count += 1
    return fib_num[n-1]
print(factorial(num) + fib(num))



# ex. => 2.4.3
nums = [input() for num in range(int(input()))]
def abs_max(*args):
    some_dict = {}
    for i in args:
        for j in i:
            sort = "".join(str(num) for num in sorted([int(i) for i in list(j) if i.isnumeric()], reverse = True))
            some_dict.update({j: int(sort)})
    some_dict = sorted(some_dict.items(), key=lambda item: item[1], reverse = True)
    return some_dict[0][0]

print(abs_max(nums))




# ex. => 2.4.4
some_list = [i.rstrip() for i in iter(input, "Поработали, и хватит")]
def check_variable(v):
    punct = ["!\"#$%&'()*+,-./:;<=>?@[\]^`{|}~¯"]
    for password in v:
        for i in punct[0]:
            if i in password:
                print("Нельзя использовать")
                break
            elif " " in password or "\t" in password:
                print("Нельзя использовать")
                break
            elif password[0].isnumeric():
                print("Нельзя использовать")
                break
        else:
            print("Можно использовать")
            continue
check_variable(some_list)




# ex. => 2.4.5
money = [int(num) for num in input().split(" ")]
if len(money) == 3: money.extend([0, 0])
elif len(money) == 4: money.append(0)
a, b, c, d, e = money
print(money)
def get_winner(a, b, c, d, e):
    some_dict = {a: "Первый", b: "Второй", c: "Третий", d: "Четвертый", e: "Пятый"}
    MAX = max(some_dict.keys())
    return some_dict[MAX]

print(get_winner(a, b, c, d, e))




# ex. => 2.4.6
some_weights = [float(i) for i in input().split(" ") if i]
def get_weight(*args):
    max_weight = int(input())
    if sum(args[0]) >= max_weight: return "Не повезло"
    else: return "Повезло"

print(get_weight(some_weights))



# ex. => 2.4.7
# sort the list of numbers in increasing order of the sum of their numbers
print(" ".join(i[0] for i in sorted({i:sum(map(int, list(i))) for i in input().split(" ")}.items(), key=lambda item: item[1])))




# ex. => 2.4.9
def shift_list(lst, shift):
    if abs(shift) <= len(lst):
        shift *= -1
        lst = lst[shift:] + lst[:shift]
    elif abs(shift) > len(lst):
        if shift < 0:
            shift *= -1
            shift = shift % len(lst)
            lst = lst[shift:] + lst[:shift]
        elif shift > 0:
            shift = shift % len(lst); shift *= -1
            lst = lst[shift:] + lst[:shift]
    return lst




# ex. => 2.4.10
def binary_to_decimal(binary):
    binary = [int(num) for num in list(binary)]
    squares = sorted([2 ** i for i in range(len(binary))], reverse = True)
    binary_dict = {squares[i]:binary[i] for i in range(len(binary))}
    return sum([i for i in binary_dict.keys() if binary_dict[i] != 0])

def decimal_to_binary(n):
    binary = ""
    if n == 0: binary += "0"
    while n > 0:
        binary += "0" if n % 2 == 0 else "1"
        n = (n-1)/2 if n%2 == 1 else n/2
    return binary[::-1]

print(decimal_to_binary(binary_to_decimal("100")))