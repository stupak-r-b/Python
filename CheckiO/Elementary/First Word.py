"""
You are given a string where you have to find its first word.

Input: A string.
Output: A string.
"""
import re


def first_word(text: str) -> str:

    # using the module "re" and function "findall" we find all the words
    list_of_words = re.findall(r"[A-Za-z']+", text)

    # returned first word of the list
    return list_of_words[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
