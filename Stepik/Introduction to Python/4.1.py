# ex. => 4.1.1
import math
a1, b1, c1 = [int(i) for i in input().split(" ")]
a2, b2, c2 = [int(i) for i in input().split(" ")]
def cos(a1, b1, c1, a2, b2, c2):
    COS = (a1*a2 + b1*b2 + c1*c2) / ((math.sqrt(a1**2 + b1**2 + c1**2))*(math.sqrt(a2**2 + b2**2 + c2**2)))
    return round(math.degrees(math.acos(COS)), 2)
print(cos(a1, b1, c1, a2, b2, c2))



# ex. => 4.1.2
from math import *
a, b = [int(i) for i in input().split(" ")]
def f(a, b):
    F =  (factorial(floor(b/a)) + a**(b*pi)) / (log2(a) * sqrt(a/b) * cos(b + exp(a)))
    return ceil(F)
print(f(a, b))



# ex. => 4.1.3
import random
nums = [int(i) for i in input().split(" ")]
value = True
count1 = 0
while value:
    random.shuffle(nums)
    count = 0
    for i in range(len(nums)-1):
        if nums[count] > nums[count+1]: break
        elif i == len(nums)-2 and nums[count] <= nums[count+1]: value = False
        count += 1
print(" ".join(str(i) for i in nums))



# ex. => 4.1.4
some_dict = {i[0]:int(i[1]) for i in [i.split("/") for i in input().split(" ")]}
for i in range(int(input())):
    for j in  [i.split("/") for i in input().split(" ")]:
        if some_dict[j[0]] == 0: break
        some_dict[j[0]] = some_dict[j[0]] - int(j[1])
print(" ".join(f"{i[0]}/{i[1]}" for i in some_dict.items()))
print("".join(sorted(some_dict.items(), key=lambda i: i[1], reverse = True)[0][0]))