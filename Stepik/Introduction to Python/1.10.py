# ex. => 1.10.1
# print in the reverse order all even numbers
some_list = []
while True:
    message = input()
    if message == ".": break
    elif int(message) % 2 == 0:
        some_list.append(message)
for num in some_list[::-1]:
    print(num, end=" ")



# ex. => 1.10.2
# find the median of this sequence
some_nums = []
while True:
    message = input()
    if message == ".": break
    some_nums.append(int(message))
some_nums = sorted(some_nums)
if len(some_nums) % 2 == 0:
    while True:
        if len(some_nums) == 2: break
        some_nums.remove(some_nums[0])
        some_nums.remove(some_nums[-1])
    median = sum(some_nums)/2
    print(median)
else:
    while True:
        if len(some_nums) == 1: break
        some_nums.remove(some_nums[0])
        some_nums.remove(some_nums[-1])
    median = some_nums[0]
    print(median)



# ex. => 1.10.3
lis = [int(input()) for i in range(int(input()))]
# find min even number and min odd number

if len(set(["even" if i%2 == 0 else "odd" for i in lis])) == 2:
    x = sorted([i for i in lis if i % 2 == 0])[0]
    y = sorted([i for i in lis if i % 2 == 1])[0]
    new = [i+(x+y) if i < (x+y) else i for i in lis]
    for i in new: print(i, end=" ")

# if not even or odd numbers in some_list
else:
    x = [i for i in lis if i % 2 == 0]; x = x[0] if x else 0
    y = [i for i in lis if i % 2 == 1]; y = y[0] if y else 0
    new = [i+(x+y) if i<(x+y) else i for i in lis]
    for i in new: print(i, end=" ")



# ex. => 1.10.4
# print the letters of the words entered in upper case, separating them with spaces
words = []
while True:
    word = input()
    if word == ".": break
    words.append("".join(i.upper() + " " for i in word))
for word in words:
    print(word.rstrip())



# ex. => 1.10.5
text = [i for i in iter(input, ".")]
some_text = " ".join(text[int(input())-1] for i in range(int(input())))
print(some_text)



# ex. => 1.10.6
text1 = [i for i in iter(input, ".")]
print(" ".join(i[len([i for i in [i.lower().split(" ") for i in text1] if "python" in i])-1] for i in text1))



# ex. => 1.10.7
# replace spaces in the string with underscores
print(input().rstrip().replace(" ", "_"))



# ex. => 1.10.10
len_str = int(input())
some_text = [i for i in iter(input, ".")]
for i in some_text:
    if len(i) > len_str:
        print(f"{i[:len_str]}... Читайте продолжение в источнике...")
    elif len(i) < len_str:
        print(f"{i}")



# ex. => 1.10.11
# numbers are entered to the point. with a space, print these numbers in reverse order, squaring them
nums = [int(i) for i in iter(input, ".")]
print(" ".join(str(i**2) for i in nums[::-1]))



# ex. => 1.10.13
some_dict = {"@@": "ошибка", "!!": "предупреждение", "//": "информация", "**": "подробное сообщение"}
while True:
    message = input()
    if message == ".": break
    for symb in some_dict.keys():
        if symb in message:
            print(f"{some_dict[symb]}")




# ex. => 1.10.14
some_list = []
while True:
    message = input().split(" ")
    if message[0] == ".":
        print(" ".join(i for i in some_list))
        break
    elif message[0] == "POST":
        some_list.append(" ". join(i for i in message[1:]))
    elif message[0] == "GET":
        print(some_list[-1])
    elif message[0] == "DELETE":
        some_list.remove(some_list[-1])



# ex. => 1.10.15
some_list = []
while True:
    message = input().split(" ")
    if message[0] == ".":
        print(" ".join(i for i in some_list))
        break
    elif message[0] == "POST":
        some_list.append(" ". join(i for i in message[1:]))
    elif message[0] == "GET":
        print(some_list[-1])
    elif message[0] == "DELETE":
        some_list.remove(some_list[-1])



# enter three integers separated by spaces. insert the desired sign between the first two numbers(+-*/) and the
# equal sigb between the second and third numbers so that the correct equality is obtained
message = [int(i) for i in input().split()]
if message[0] + message[1] == message[2]:
    print(f"{message[0]} + {message[1]} = {message[2]}")
elif message[0] - message[1] == message[2]:
    print(f"{message[0]} - {message[1]} = {message[2]}")
elif message[0] * message[1] == message[2]:
    print(f"{message[0]} * {message[1]} = {message[2]}")
elif message[0] != 0:
    if message[0] / message[1] == message[2]:
        print(f"{message[0]} / {message[1]} = {message[2]}")
    else:
        print("Error")
else:
    print("Error")