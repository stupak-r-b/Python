# ex. => 3.1.1
def f(x):
    if x <= -2:
        x = 1 - (x + 2)**2
    elif -2 < x <= 2:
        x = -x/2
    else:
        x = (x - 2)**2 + 1
    return x



# ex. => 3.1.2
# write the function, which takes a list of integers as an input, removes all odd values
# from it, and evenly divides even numbers by two. The function should not return anything,
# only a change to the transferred list is required

def modify_list(l):
    # copy the list
    x = l[:]
    # delete odd numbers
    x = [int(num/2) for num in x if num % 2 == 0]
    # delete all numbers from 'l' list
    for item in range(len(l)):
        l.remove(l[0])
    # copy the 'x' list to the 'l' list
    for i in x:
        l.append(i)