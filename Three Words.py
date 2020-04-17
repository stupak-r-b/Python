"""
    You are given a string with words and numbers separated by whitespaces. THe words contains only
letters. You should check if the string contains three words in succession.

Input: A string with words.
Output: The answer as a boolean.
"""
import re


def checkio(words: str) -> bool:
    some = "[A-Za-z]+ [A-Za-z]+ [A-Za-z]+"
    x = re.findall(some, words)
    return True if x else False


if __name__ == '__main__':

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
