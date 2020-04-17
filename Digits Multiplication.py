"""
You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.
For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.
Output: The product of the digits as an integer.
"""

from numpy import prod


def checkio(number: int) -> int:
    list_of_num = [int(i) for i in str(number) if i != "0"]     # add numbers to the list
    return int(prod(list_of_num))                               # using numpy multiply all the numbers


if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
