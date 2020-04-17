# ex. => 2.5.1
# write Ackerman function
N = int(input())
M = int(input())
def A(m, n):
    if m == 0: return n + 1
    if m > 0 and n == 0: return A(m - 1, 1)
    if m > 0 and n > 0: return A(m-1, A(m, n-1))

print(A(M, N))




# ex. => 2.5.2
# write a recursive function digits (n) that takes a natural number and terurns a string with the digits
# of tha number from left to right, separated by spaces
def digits(n):
    return n if len(str(n)) == 1 else str(n)[0] + " " + digits(str(n)[1:])

print(digits(14623))



# ex. => 2.5.3
# write a recursive function get_length(obj) that takes an iterable object as input and displays its length
def get_length(obj, count = 0):
    count += 1
    return count - 1 if not obj else get_length(obj[1:], count)




# ex. => 2.5.4
some_list = [1, 1]
count = 0
def fib(n):
    global count
    if n == 1 or n == 2: return 1
    some_list.append(some_list[count]+some_list[count+1])
    count += 1
    return fib(n) if count != n-2 else some_list[-1]



# ex. => 2.5.5
# write a recursive function is_power(n) that returns True
# if the passed natural number is a power of two, and False otherwise
def is_power(n):
    if n == 0 or n == 1: return True
    return False if n < 1 else is_power(n / 2)




# ex. => 2.5.6
# write a recursive funcion get_pow(a, n) that raises the number a to the power n
def get_pow(a, n, num = 1):
    if n == 0 or a == 1: return 1
    if a == 0: return 0
    if n == 1: return num*a
    elif n > 1: return get_pow(a, n-1, num*a)




# ex. => 2.5.7
# recursive fibonacci function
some_list = [1, 1]
count = 0
def fib(n):
    global count
    if n == 1 or n == 2: return 1
    some_list.append(some_list[count]+some_list[count+1])
    count += 1
    return fib(n) if count != n-2 else some_list[-1]