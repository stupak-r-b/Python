#   ex. => 2.3.1 => multiplication table fragment

#   Example:
#   Sample Input 1:
#
#   7
#   10
#   5
#   6
#
#   Sample Output 1:
#
#   	5	6
#   7	35	42
#   8	40	48
#   9	45	54
#   10	50	60

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print("\t" + "\t".join(str(num) for num in range(c, d+1)))
for num in range(a, b+1):
    print(f"{num}\t" + "".join(str(num*nums)+"\t" for nums in range(c, d+1)))


# ex. 2.3.2

# write a program that reads two numbers "a" and "b" from the arithmetic mean of all numbers
# from the segment [a; b], which are divided by 3.
a = int(input())
b = int(input())
some_list = [num for num in range(a, b+1) if abs(num) % 3 == 0]
print(sum(some_list)/len(some_list))
