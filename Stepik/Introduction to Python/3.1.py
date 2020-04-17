# ex. => 3.1.1
# create empty dictionary
dictionary = {}

# create a loop
while True:

# using split method create a list
    message = input().split(" ")
    if message[0] == ".": break

# message[0] is key
    elif len(message) == 1:
        print(dictionary.get(message[0]))

# mesage[0] is key, message[1] is value
    elif len(message) == 2:
        dictionary.update({message[0]:message[1]})




# ex. => 3.1.2
# print the word that occurs most often in the text, and the number of its
# occurrences separated by a space
text = input().lower().split(" ")
dictt = {}
for word in text:
    for item in ",.?!":
        if item in word:
            word = word.replace(item, "")

# if word in the dictionary values + 1
    dictt[word] = dictt.get(word, 0) + 1

dictt = sorted(dictt.items(), key = lambda item: item[1])

# print the word that occurs most often in the text
print(dictt[-1][0], dictt[-1][1])



# ex. => 3.1.3
# dictionary of programers

# create some dictionary using method split and iterator
some_dictionary = {j[0]:j[1] for j in [i.split(" – ") for i in iter(input, ".")]}

# print values if dictionary using get() method and range() function
print("\n".join(some_dictionary.get(input(), "Не найдено") for i in range(int(input()))))




# ex. => 3.1.4
# access right program
access_right = {"admin": {"read":["system", "confidential", "settings", "ordinary"], "edit": ["system", "confidential", "settings", "ordinary"]},
                   "experienced": {"read":["system", "settings", "ordinary"], "edit": ["confidential", "ordinary"]},
                   "user": {"read":["ordinary"], "edit": ["ordinary"]}}
some_dictionary = dict([tuple(i) for i in [i.split(" ") for i in iter(input, ".")]])
while True:
    request = input().split(" ")
    if request[0] == ".": break
    elif some_dictionary[request[0]] in access_right[request[2]][request[1]]:
        print("Access granted")
    else:
        print("Access denied")




# ex. => 3.1.5
dictionary = {}
while True:
    message = input().replace(",", "").split(" ")
    if message[0] == "." : break
    elif len(message) == 1: print("Не найдено") if message[0] not in dictionary else \
    print("".join(i+", " if i != dictionary.get(message[0])[-1] else i for i in dictionary.get(message[0])))
    elif len(message) > 1: dictionary.update({message[0]:message[1:]}) \
    if message[0] not in dictionary else [dictionary[message[0]].append(i) for i in message[1:]]




# ex. => 3.1.6
country = {}
capital = {}
while True:
    text = input().split(":")
    if len(text) == 1: break
    else: country[text[1].strip()] = text[0]; capital[text[0]] = text[1].strip()
while True:
    some_title = input()
    if some_title == ".": break
    elif some_title in country: print(country[some_title])
    elif some_title in capital: print(capital[some_title])
    else: print("Нет данных")




# ex. => 3.1.7
# Morse Code
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}

ezrom = {'•—': 'a', '—•••': 'b', '—•—•': 'c', '—••': 'd', '•': 'e', '••—•': 'f', '——•': 'g', '••••': 'h',
         '••': 'i', '•———': 'j', '—•—': 'k', '•—••': 'l', '——': 'm', '—•': 'n', '———': 'o', '•——•': 'p',
         '——•—': 'q', '•—•': 'r', '•••': 's', '—': 't', '••—': 'u', '•••—': 'v', '•——': 'w', '—••—': 'x',
         '—•——': 'y', '——••': 'z'}

some_think = input().lower()
if some_think[0] == "—" or some_think[0] == "•":
    some_think = [["".join(i for i in [ezrom[j] for j in i])] for i in [i.split(" ") for i in some_think.split("\t")]]
    some_think = " ".join(j for i in some_think for j in i)
    print(some_think)
elif some_think[0].isalpha():
    text = ""
    for word in some_think.split(" "):
        w = ""
        for letter in word:
            w += morze[letter] + " "
        text += w.strip() + "\t"
    print(text.strip())




# ex. => 3.1.8
some_things, start_price = input(), int(input())
bidders = [i for i in input().split(", ")]
some_dict = {i:[start_price] for i in some_things.split(", ")}
while True:
    bidding = input()
    if bidding == "Аукцион закончен!": break
    for item in some_dict:
        if item in bidding:
            bidding = bidding.replace(item, "").split("  ")
            if some_dict[item][0] < int(bidding[1]) and bidding[0] in bidders:
                some_dict[item][0] = int(bidding[1])
                some_dict[item].append(bidding[0])
print("\n".join(i + " " + str(some_dict[i][-1]) + " " + str(some_dict[i][0]) if len(some_dict[i]) > 1
      else i + " " + "Предложений не было" for i in some_dict.keys()))







# ex. => 3.1.9
libary = [i.replace('" ', ",").replace(' "', ",").replace("(", "").replace(")", "").split(",") for i in input().split(", ")]
new_libary = {}
read_by_users = {}
favorite_genre = {}
value = True

# create database 'new_libary' and distribute films by genre
for item in libary:
    if item[-1] in new_libary: new_libary[item[-1]].append(item[1])
    elif item[-1] not in new_libary: new_libary[item[-1]] = [item[1]]

# cycle for distributing movies by favorite user genres
while value:
    request = input()
    if request == ".": break
    request = request[:-1].split(" (") if "(" in request else request[:-1].split(' "')
    if request[0] == "Посоветуй мне книгу":
        favorite_genre = {i[0]: sorted({j[0]: len(j[1]["finished"]) if j[1]["unread"] else 0 for j in i[1].items()}.items(), key= lambda item: item[1], reverse=True) for i in read_by_users.items()}

# if there is only one favorite genre
        if request[1] in favorite_genre and len(favorite_genre[request[1]]) == 1:

# if the servise has nothing more to offer the user
            if not read_by_users[request[1]][favorite_genre[request[1]][0][0]]['unread']:
                print("Список пуст")
                continue

# if the user has only one favorite genre and service recommend more books to the user
            print(", ".join(f"\"{i}\"" for i in read_by_users[request[1]][favorite_genre[request[1]][0][0]]['unread']))

# if the user has more than one favorite genre
        elif request[1] in favorite_genre and len(favorite_genre[request[1]]) > 1:
            count = 0
            recommendation = ""
            for favor in favorite_genre[request[1]]:
#  if the user if equally fond of several genres
                if favor[1] == favorite_genre[request[1]][0][1]:
                    recommendation += ", ".join(f"\"{i}\"" for i in read_by_users[request[1]][favor[0]]['unread']) + ", "
                    continue
            for i in  read_by_users[request[1]]:
                if not read_by_users[request[1]][i]["unread"]:
                    count += 1

# if the user has read all books in all favorite genres
            if count == len(favorite_genre[request[1]]):
                print("Список пуст")
            else:
                print(recommendation[:-2])

# if the user has not read a single book
        else:
            print("Список пуст")

# create database 'read_by_users' of users favorite genres, and distribute
# movies by genre
    elif request[0] != "Посоветуйте мне книгу":

# if the user is already in the database
        if request[0] in read_by_users:
            for genre in new_libary:
                if request[1] in new_libary[genre]:

# if the user is added to the database and his favorite genre is also
                    if genre in read_by_users[request[0]] and request[1] in read_by_users[request[0]][genre]["unread"]:
                        read_by_users[request[0]][genre]["finished"].append(request[1])
                        read_by_users[request[0]][genre]["unread"].remove(request[1])
# if the user is added to the database BUT the user has a new favorite genre
                    elif genre not in read_by_users[request[0]]:
                        unread = new_libary[genre][:]; unread.remove(request[1])
                        read_by_users[request[0]].update({genre:{"finished": [request[1]], "unread": unread}})

# elif need to create new user
        elif request[0] not in read_by_users:
            for genre in new_libary:
                if request[0] and request[1] in new_libary[genre]:
                    unread = new_libary[genre][:]; unread.remove(request[1])
                    read_by_users[request[0]] = {genre:{"finished": [request[1]], "unread": unread}}




# ex. => 3.1.10
phone_book = {}
while True:
    text = ""; count = 0
    for i in input():
        if i == " " and count == 0: count += 1; text += "," + i
        text += i
    text = ["".join(i for i in i.strip() if i not in "+- ()") for i in text.split(", ")]
    if text[0] == ".": break
    elif len(text) == 1 and text[0] in phone_book:
        if phone_book[text[0]]: print(", ".join(i for i in phone_book[text[0]])); continue
        else: print("Не найдено"); continue
    elif len(text) == 1 and text[0] not in phone_book: print("Не найдено"); continue
    elif len(text) > 1:
        for item in text:
            if len(item) == 11 and item[0] in "78" and text[0] not in phone_book:
                item = f"+7 ({item[1:4]}) {item[4:7]}-{item[7:9]}-{item[9:]}"
                phone_book[text[0]] = [item]; continue
            elif len(item) == 11 and item[0] in "78" and text[0] in phone_book:
                item = f"+7 ({item[1:4]}) {item[4:7]}-{item[7:9]}-{item[9:]}"
                phone_book[text[0]].append(item); continue




# ex. => 3.1.11
# encrypt the word
encrypted = {}; word = input()
for i in word:
    if i not in ",.–- ()?!+-=#@$%^&*><":
        encrypted.update({i: encrypted.get(i, 0) + 1})
print(encrypted)
letter = {i[1]: i[0] for i in [j.split(": ") for j in [i for i in iter(input, ".")]]}
encrypted = {i[0]: letter[str(i[1])] for i in encrypted.items()}
print("".join(encrypted[i] if i in encrypted else i for i in word))



