# ex. => 3.2.1
# count duplicate items

# create some list with different data
some_data = input().split(" ")

# count and print length list and length set(list)
print(len(some_data) - len(set(some_data)))




# ex. => 3.2.4
T, H = [set([float(j) for j in i.split(" ")]) for i in [input() for i in range(2)]]
print("Корректно" if 100/len(T) * len(T&H) > 70 else "Некорректно")




# ex. => 3.2.6
some_list = [set([i for i in input().split(", ")]) for i in range(int(input()))]
while len(some_list) != 1:
    some_list[0] = some_list[0]&some_list[1]
    some_list.remove(some_list[1])
print(", ".join(i for i in some_list[0])) if some_list[0] else print("Фильм снять не удастся:(")