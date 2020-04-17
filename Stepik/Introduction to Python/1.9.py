# ex. => 1.9.1
# write a program that in a sequence of natural numbers determines the minimum number ending in 4
some_list = [int(i) for i in [input() for num in range(int(input()))] if i[-1] == "4"]
print(min(some_list))



# ex. => 1.9.2
# write a program that in a sequence of natural numbers determines the sum of numbers that are multiples of 6
SUM= sum([i for i in [int(input()) for num in range(int(input()))] if i % 6 == 0])
print(SUM)



# ex. => 1.9.3
some_tuple = [int(i) for i in list(input().split(" "))]
count1 = 0; count2 = 0
for num in some_tuple:
    if num == some_tuple[-1]: break
    elif (some_tuple[count1] + some_tuple[count1 + 1]) % 9 != 0:
        if (some_tuple[count1] + some_tuple[count1 + 1]) % 3 == 0: count2 += 1
    count1 += 1
print(count2)


# ex. => 1.9.4
# write a program that allows you to find and display the maximum value among the two-digit elements
# of a tuple that are not divisible by 3
some_tuple = [int(i) for i in list(input().split(" ")) if len(i) == 2 and int(i) % 3 != 0]
if some_tuple: print(max(some_tuple))
else: print("Не найдено")



# ex. => 1.9.5
# a tuple containing 40 real numbers is given. write a program that allows you to find in this tuple two
# neighboring elements whose values are the least close
some_list = [float(i) for i in list(input().split(" "))]
new_list1 = []; new_list2 = {}
count = 0
for num in some_list:
    if num == some_list[-1]: break
    else:
        new_list1.append([some_list[count], some_list[count+1]])
        new_list2.update({count:abs([some_list[count] - some_list[count+1]][0])})
    count += 1
new_list2 = sorted(new_list2.items(), key=lambda item: item[1])
print(new_list1[new_list2[-1][0]][0], new_list1[new_list2[-1][0]][1])
