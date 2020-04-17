"""
    Here you should find the length of the longest substring that consists of the same letter.
For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c"
and "aaaa". The last substring is the longest one, which makes it the answer.
"""
import re


def long_repeat(line: str) -> int:

    # using "re" we found lines wich contains same symbols and add to the list
    lenth = [re.findall(f"{i}*", line) for i in set(line)]

    # items that returned "True" are added to the list
    some_list = [j for i in lenth for j in i if bool(j)]

    # returns the longest substring
    return max(len(i) for i in some_list) if line != "" else 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
