# ex. => 1.8.1
some_text = [input() for text in range(int(input()))]

# position in some_text list
count1 = 1

# count in "rat" in text
count2 = 0
for text in some_text:
    if "rat" in text:
        print(count1)
        count2 += 1
    count1 += 1
if count2 == 0:
    print("-1")



# ex. => 1.8.2
# print the sum of numbers entered to zero
some_numbers = []
while True:
    num = int(input())
    if num == 0: break
    some_numbers.append(num)
print(sum(some_numbers))