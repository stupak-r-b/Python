"""
    For the input of your function, you will be given one sentence. You have to return a corrected version,
that starts with a capital letter and ends with a period (dot).Pay attention to the fact that not all of the
fixes are necessary. If a sentence already ends with a period (dot), then adding another one will be a mistake.

Input: A string.
Output: A string.


"""


def correct_sentence(text: str) -> str:

    # capitalize the first letter of word
    text = text[0].upper() + text[1:]

    # if there is no point at the end of the word add a point
    return text + "." if text[-1] != "." else text


if __name__ == '__main__':

    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
