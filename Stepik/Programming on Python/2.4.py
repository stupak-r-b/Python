# ex. => 2.4.1
# write a program that calculates the percentage of G and C characters in a string

text = input()
count = 0
for letter in text:
    if letter.lower() == "c" or letter.lower() == "g":
        count += 1
precentage = (count/len(text)) * 100
print(float(precentage))


# ex. => 2.4.2
# groups of indentical characters of the original string are replace by this
# character and the number of it's repetitions
s = input()
new_text = ""
count = 1
for i in s:

    # if letter == next letter
    if len(s) > 1 and s[0] != s[1]:
        new_text += s[0] + str(count)
        s = s[1:]
        count = 1

    # if letter != next letter
    elif len(s) > 1 and s[0] == s[1]:
        count += 1
        s = s[1:]

    # if len s < 2
    else:
        new_text += s[0] + str(count)
        break

print(new_text)
