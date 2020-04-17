# write a program that reads integers from standard input, one number per line,
# and after the first zero entered, displays the sum of the numbers received at the input
num = ""
summ = 0
while num != 0:
    num = int(input())
    summ += num
print(summ)




# find the least common multiple
first_group  = int(input())
second_group = int(input())
num = 0
while True:
    num += 1
    if num % first_group == 0 and num % second_group == 0:
        print(num)
        break