"""
Input: The text and the search words array.
Output: The dictionary where the search words are the keys and values are
        the number of times when those words are occurring in a given text.
"""


def popular_words(text, words):

    # added to "some_list" lowercase word from text
    some_list = [x.lower() for x in text.split() if x.lower() in words]

    # count the elements in the text from "words" and add to the "some_dict"
    some_dict = {x: some_list.count(x) for x in words}
    return some_dict


if __name__ == '__main__':

    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
