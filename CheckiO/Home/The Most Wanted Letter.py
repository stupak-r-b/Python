"""
Input: A text for analysis as a string.
Output: The most frequent letter in lower case as a string.
"""


def checkio(text: str) -> str:

    # add letters to the list if element is letter
    new = [i for i in text.lower() if i.isalpha()]
    new.sort()

    # add the number of entries to the list
    letter = [new.count(i) for i in new]

    max_index = letter.index(max(letter))
    return new[max_index]


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
