"""
    There is a list which contains integers or other nested lists which may contain yet more lists and integers
which then… you get the idea. You should put all of the integer values into one flat list. The order should be
as it was in the original list with string representation from left to right.
"""

import re


def flat_list(a):

    # converted the array to the string
    w = "".join(i + "," for i in list(map(lambda x: str(x), a)))

    # returned the string without non-alphabetic elements except a comma
    return [int(i) for i in re.findall("[\-\d]+", w)]


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [
        2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
