"""
Given a list of numbers, you should find the sum of these numbers. Your solution should not contain any of the banned
words, even as a part of another word. The list of banned words are as follows:

sum
import
for
while
reduce

Input: A list of numbers.
Output: The sum of numbers.
"""


def checkio(n):
    n[0] += n[len(n)-1] if len(n) > 1 else 0
    if len(n) == 1: return n[0]
    return n[0] if len(n)-1 == 1 else checkio(n[:len(n)-1])
