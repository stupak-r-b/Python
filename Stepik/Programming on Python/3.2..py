# ex. => 3.2.1
def update_dictionary(d, key, value):

# if the key is in the 'd' dictionary, then add the value to the list that is stored by this key
    if key in d.keys():
        d[key].append(value)
    elif key not in d.keys():

# if the key is not in the word, you need to add the value to the list bt the key '2*key'
        if key * 2 in d.keys():
            d[key*2].append(value)

# if the key '2*key' is not present, then you need to add the key '2*key' to the
# dictionary and then add a new item to the list which is the value
        elif key * 2 not in d.keys():
            d[key*2] = [value]


# ex. => 3.2.2
# the program should read one line from standard input and output for each unique word in thes
# line the number of repetitions (case insensitive) in the format "word quantity"
text = input()
def unique(txt):
    txt = txt.lower().split(" ")
    dictionary = {}
    for item in txt:
        dictionary[item] = txt.count(item)
    return dictionary

# information output cycle
for key, value in unique(text).items():
    print(f"{key} {value}")



# ex. => 3.2.3
some_list = [int(input()) for i in range(int(input()))]
some_dict = {}
for i in some_list:
    if i not in some_dict: some_dict.update({i: i*13})
for i in some_list: print(f"{some_dict[i]}")

