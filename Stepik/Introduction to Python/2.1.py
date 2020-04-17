# ex. => 2.1.1
# remove all whitespace sequences from the ends of the line and print their number.
# you cannot use the split() mothod
some_text = input()
space = ""
while True:
    if some_text[0] == " " or some_text[0] == "\t":
        space += some_text[0]
        some_text = some_text[1:]
    if some_text[-1] == " " or some_text[-1] == "\t":
        space += some_text[-1]
        some_text = some_text[:-1]
    if some_text[0] != " " and some_text[-1] != " ": break
print(some_text)
print(len(space))




# ex. => 2.1.2
# remove duplicate characters from string
some_text = input()
new_text = ""
for i in some_text:
    if i not in new_text:
        new_text += i
print(new_text)




# ex. => 2.1.3
# print the sum of the indices of the minimum number of a sequence
some_text = [int(i) for i in input().split(",")]
MIN = min(some_text)
count = 0
some_dict = {}
for i in some_text:
    if i not in some_dict:
        some_dict[i] = [count]
        count += 1
    elif i in some_dict:
        some_dict[i].append(count)
        count += 1
print(sum(some_dict[MIN]))




# ex. => 2.1.4
# print each line with inverted case
some_text = []
while True:
    txt = input()
    if txt.isupper() or txt.islower() or txt.isnumeric(): break
    some_text.append(txt)

for i in some_text:
    print(i.swapcase())



# ex. => 2.1.5
# replace each digit n in the string with the digit (n + 1), with the digit 9 changing to 0.
some_text = input()
new_text = ""
count = 0
for i in some_text:
    if i.isnumeric():
        if int(i) == 9:
            new_text += "0"
        elif int(i) != 9:
            new_text += str(int(i)+1)
            count += int(i)+1
    else:
        new_text += i
print(new_text)
print(count)



# ex. 2.1.6
# count the number of numbers equal to the maximum of the sequence
some_text = [int(i) for i in input().split(",")]
print(some_text.count(max(some_text)))



# ex. 2.1.7
# print the two largest modulo numbers
some_text = sorted([int(i) for i in input().split(",")], key = lambda i: abs(i))
print(some_text[-2], some_text[-1])




# ex. 2.1.8
nums = [int(i) for i in input().split(" ") if i]
lenth = int(len(nums)/2)
left = sorted(nums[:lenth])
right = sorted(nums[lenth:], reverse=True)
print(left[0] + right[-1])




# ex. 2.1.9
# determine if the entered string is a palindrome
some_text = input().lower().replace(" ", "")
same_text = some_text[::-1]
if some_text == same_text : print("YES")
else: print("NO")




# ex. 2.1.10
some_text = [int(i) for i in input().replace(",", "").split(" ")]
episode = int(input()); some_text.append(episode); new = []
some_text.sort()
for i in some_text:
    if i in new: continue
    new.append(i)

print(len(new)-1)
for i in range(len(new)):
    if new[i] == episode:
        print(new[i+1])
        break