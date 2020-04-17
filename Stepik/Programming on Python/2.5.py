# ex. => 2.5.1
# write a program that inputs one line with integers.
# the program should print the sum of these numbers
numers = input()
print(sum([int(num) for num in numers.split(" ")]))



# ex. => 2.5.2
# write a program, the input is a list of numbers in one line. The program should display the sum of its
# two neighbors for each element of this list
txt = [int(num) for num in input().split(" ")]
lenth = len(txt)
new_text = ""
if lenth > 1:
    for num in range(lenth):
        if num == 0:
            new_text += str(txt[1] + txt[-1]) + " "
        elif num == lenth - 1:
            new_text += str(txt[-2] + txt[0])
        else:
            new_text += str(txt[num - 1] + txt[num + 1]) + " "
    print(new_text)
else:
    new_text += str(txt[0])
    print(new_text)



# ex. => 2.5.3
# write a program that takes a list of numbers in one line as input and displays balues that are
# repeated in it more than once on the screen in one line
string = input().split(" ")
new_string = [num for num in string if string.count(num) > 1]
print(" ".join(num for num in list(set(new_string))))