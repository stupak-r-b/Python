"""
    Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of
times they appear in elements. If two elements have the same frequency, they should end up in the same order as the
first appearance in the iterable.
"""


def frequency_sort(items):
    # counting same elements in array and add to the dictionary
    dictt = {i: items.count(i) for i in items}

    # added unique elements to the list
    count = [i[0] for i in sorted(dictt.items(), key=lambda kv: kv[1], reverse=True)]

    # returns sorted elements
    return [i for i in count for j in range(items.count(i))]


if __name__ == '__main__':

    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
