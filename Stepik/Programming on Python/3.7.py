# ex. => 3.7.1
# input list
some_list = [int(input())]

# until the length of the list is equal to the first element of the list
count = 1
while count != some_list[0]+1:
    item = input()
    some_list.append(item.split(";"))
    count += 1

# number of victories
victories = {}
for i in some_list[1:]:
    if i[0] in victories:
        if int(i[1]) > int(i[3]):victories[i[0]].append("win")
        elif int(i[1]) < int(i[3]):victories[i[0]].append("lose")
        else:victories[i[0]].append("draw")
    if i[0] not in victories:
        if int(i[1]) > int(i[3]): victories[i[0]] = ["win"]
        elif int(i[1]) < int(i[3]): victories[i[0]] = ["lose"]
        else: victories[i[0]] = ["draw"]
    if i[2] in victories:
        if int(i[3]) > int(i[1]):victories[i[2]].append("win")
        elif int(i[3]) < int(i[1]):victories[i[2]].append("lose")
        else:victories[i[2]].append("draw")
    if i[2] not in victories:
        if int(i[3]) > int(i[1]):victories[i[2]] = ["win"]
        elif int(i[3]) < int(i[1]):victories[i[2]] = ["lose"]
        else:victories[i[2]] = ["draw"]

# total games
new_list = [j for i in some_list[1:] for j in i if not j.isnumeric()]
total_games = {i:new_list.count(i) for i in new_list}

# information output cycle
for i in set(new_list):
    print(f"{i}:{total_games[i]} {victories[i].count('win')} {victories[i].count('draw')}"
          f" {victories[i].count('lose')} {victories[i].count('win') * 3 + victories[i].count('draw')*1}")



# ex. => 3.7.2
word = [i for i in input()]
keys = [i for i in input()]
a = input()
b = input()
count = 0
encypt = {}
for i in word:
    encypt[i] = keys[count]
    count += 1

count = 0
decipher = {}
for i in keys:
    decipher[i] = word[count]
    count += 1

# encrypt the word
new_word = "".join(encypt[i] for i in a)

# decipher the word
another_word = "".join(decipher[i] for i in b)

print(new_word)
print(another_word)



# ex. => 3.7.3
words1 = [word.lower() for word in [input() for i in range(int(input()))]]
words2 = {j.lower() for i in [word.split(" ") for word in [input() for i in range(int(input()))]] for j in i}
errors = {i for i in words2 if i not in words1}
for word in errors:
    print(word)



# ex. => 3.7.4
# write a program displays the point where the turtle will be after all the commands

# the distance that the turtle has traveled in relation to all sides of the world
dictionary = {}
for i in range(int(input())):
    data = input().split(" ")
    if data[0] in dictionary:
        dictionary[data[0]] += int(data[1])
    elif data[0] not in dictionary:
        dictionary[data[0]] = int(data[1])

# turtle starting coordinates
coords = [0, 0]
if "восток" in dictionary:
    coords[0] += dictionary["восток"]
if "запад" in dictionary:
    coords[0] -= dictionary["запад"]
if "север" in dictionary:
    coords[1] += dictionary["север"]
if "юг" in dictionary:
    coords[1] -= dictionary["юг"]

print(f"{coords[0]} {coords[1]}")



# ex. => 3.7.5
# write a program that reads this file and calculates the average student height for each class
with open("txt.txt", "r", encoding="utf-8") as f:
    some_list = f.readlines()

# school classes
class_dict = {i for i in range(1, 12)}

# student information: class, last name, height
some_list = [i.replace("\n", "").split("\t") for i in some_list]

# class and number of students from this class about whom information is submitted
count_dict = {}
for i in range(1, 12):
    count = 0
    for j in some_list:
        if str(i) in j:
            count+=1
    count_dict[str(i)] = count

# total growth of all students in one class
total_dict = {}
for info in some_list:
    if info[0] in total_dict:
        total_dict[info[0]] += int(info[2])
    elif info[0] not in total_dict:
        total_dict[info[0]] = int(info[2])


# average height of all students in one class
for clas in range(1, 12):
    if str(clas) in total_dict:
        print(f"{clas} {total_dict[str(clas)]/count_dict[str(clas)]}")
    else:
        print(f"{clas} -")