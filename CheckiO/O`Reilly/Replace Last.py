from typing import Iterable

# in a given list the last element should become the first one. 
#An empty list or list with only one element should stay the same

def replace_last(items: list) -> Iterable:
    return [items[-1]] + items[:-1] if items else []


if __name__ == '__main__':
    print("Example:")
    print(list(replace_last([2, 3, 4, 1])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
    assert list(replace_last([1])) == [1]
    assert list(replace_last([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
