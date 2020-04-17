"""
    In this mission you should write a function that introduces a person with the given parameter's attributes.

    Input: Two arguments. String and positive integer.

    Output: String.
"""


def say_hi(name: str, age: int) -> str:
    return "Hi. My name is {0} and I'm {1} years old".format(name, age)


if __name__ == '__main__':
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')
