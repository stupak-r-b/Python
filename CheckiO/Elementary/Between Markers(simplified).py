"""
    You are given a string and two markers (the initial one and final). You have to find
a substring enclosed between these two markers. But there are a few important conditions.

- This is a simplified version of the Between Markers mission.
- The initial and final markers are always different.
- The initial and final markers are always 1 char size.
- The initial and final markers always exist in a string and go one after another.

Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
Output: A string.
"""


def between_markers(text: str, begin: str, end: str) -> str:
    initial = text.index(begin)
    final = text.index(end)
    return text[initial + 1:final]


if __name__ == '__main__':

    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
