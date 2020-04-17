"""
You are given a string where you have to find its first word.

Input: A string.
Output: A string.
"""


def first_word(text: str) -> str:
    return text.split()[0]


if __name__ == '__main__':

    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")
