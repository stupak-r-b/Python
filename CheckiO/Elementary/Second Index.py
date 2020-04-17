"""
You are given two strings and you have to find an index of the second occurrence of the second string in the first one.

Input: Two strings.
Output: Int or None
"""


def second_index(text: str, symbol: str) -> [int, None]:
    count = 0
    some_list = []

    # all indices of the "s" symbol are added to the list
    for i in text:
        if symbol == i:
            some_list.append(count)
        count += 1

    # returned second index of the "s" symbol
    return some_list[1] if len(some_list) > 1 else None


if __name__ == '__main__':

    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
