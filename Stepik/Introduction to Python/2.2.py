# ex. 2.2.1
# create a list with input data
nums = [int(i) for i in input().split(" ")]

# list of range of numbers nums[:2] cubed
nums = [i**nums[-1] for i in range(nums[0], nums[1]+1)]

# print numbers cubed
for num in nums:
    print(num, end=" ")



# ex. 2.2.2
places = [input().split(", ") for i in range(int(input()))]
some_list = []
for item in places:
    temporary = {}
    for el in item:
        el = [int(i) if i.isnumeric() else i for i in el.split()]
        temporary.update({el[0]:el[1]})
    some_list.append({key: value for key, value in sorted(temporary.items(), key=lambda i: i[1])})

for item in some_list:
    for key, value in item.items():
        if item == some_list[-1]:
            print(key)
            break
        print(key, end = ", ")
        break



# ex. => 2.2.3
# add the information to the list
hour, max_popul = [int(i) for i in input().split(" ")]

# add ifo about different bacterial population to the another list
popul_0 = [int(i) for i in input().split(", ")]

# add surving bacterial population to the list
finish = []
for popul in popul_0:
    counter = 0
    for time in range(hour):
        popul *= 2
        counter += 1
        if counter == hour and popul <= max_popul:
            finish.append(popul)

print(len(finish))



# ex. => 2.2.4
# sort the list without using the sort() method
some_data = [int(i) for i in input().split(" ")]
sorted_list = []
while True:
    if len(some_data) == 0: break
    MAX = some_data.pop(some_data.index(max(some_data)))
    sorted_list.append(MAX)
print(" ".join(str(i) for i in sorted_list))



# ex. => 2.2.6
# sort the list without using the sort() method
some_data = [int(i) for i in input().split(" ")]
print(" ".join(str(i) for i in [some_data.pop(some_data.index(min(some_data))) for i in range(len(some_data))]))






