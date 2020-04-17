# ex. => 3.3.1
some_commands = [i for i in iter(input, "Релиз!")]
bugs = []; features = []; design = []
def add(x, defect):
    x.append(defect)
def delete(x):
    x.remove(x[-1])

for command in some_commands:
    if "Добавить" in command:
        command = command.split(": ")
        item = command[0]
        if "bugs" in item: add(bugs, command[1])
        elif "features" in item: add(features, command[1])
        elif "design" in item: add(design, command[1])
    elif "Убрать" in command:
        if "bugs" in command: delete(bugs)
        elif "features" in command: delete(features)
        elif "design" in command: delete(design)

print(bugs[-1]) if bugs else print("Все исправлено!")
print(features[-1]) if features else print("Все исправлено!")
print(design[-1]) if design else print("Все исправлено!")




# ex. => 3.3.2
some_list = sorted([j.split(". ") for j in [input() for i in range(int(input()))]], key=lambda i: int(i[1].replace(":", "")))
to_do_list = []; count = 0
for item in some_list:
    if "00:00" in item[1]:
        some_list.append(item)
        del some_list[count]
    count += 1
def add(x, command): x.append(command)
def delete(x, command): x.remove(command)
for item in some_list:
    if "Добавить" in item[0]:
        item = item[0].split(": ")
        add(to_do_list, item[1])
    if "Выполнить" in item[0]:
        item = item[0].split(": ")
        delete(to_do_list, item[1])
print(", ".join(i for i in to_do_list)) if to_do_list else print("Все выполнено!")




# ex. => 3.3.2
# reverse polish notation
nums = []
polish_notation = input().split(" ")
for symbol in polish_notation:
    if symbol.isnumeric():
        nums.append(int(symbol))
    elif not symbol.isnumeric():
        if symbol == "+":
            nums.append(nums.pop(len(nums)-2) + nums.pop(len(nums)-1))
        elif symbol == "-":
            nums.append(nums.pop(len(nums)-2) - nums.pop(len(nums)-1))
        elif symbol == "*":
            nums.append(nums.pop(len(nums)-2) * nums.pop(len(nums)-1))
        elif symbol == "/":
            nums.append(nums.pop(len(nums)-2) / nums.pop(len(nums)-1))

print(nums[0])





# ex. => 3.3.3
# the correct bracket sequence
some_dict = {"(": ")", ")": "(", "{": "}", "}": "{", "[": "]", "]": "["}
some = input()
for i in some:
    if "{}" in some: some = some.replace("{}", "")
    elif "[]" in some: some = some.replace("[]", "")
    elif "()" in some: some = some.replace("()", "")
print("NO") if some else print("YES")




# ex. => 3.3.5
closed = int(input())
prsn_pr_hour = int(input())
turn = []
while True:
    client = input()
    if client == ".": break
    elif client == "VIP-customer":
        if len(turn) % 2 == 0:
            x = len(turn)/2
            turn = turn[:int(x)] + [client] + turn[int(x):]
        elif len(turn) % 2 == 1:
            x = (len(turn)+1)/2
            turn = turn[:int(x)] + [client] + turn[int(x):]
    else: turn.append(client)
print(len(turn[closed*prsn_pr_hour:]))
print(turn[closed*prsn_pr_hour:].count("VIP-customer"))