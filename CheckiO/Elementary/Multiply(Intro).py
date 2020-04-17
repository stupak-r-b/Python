"""
        This is an intro mission, the purpose of which is to explain how to solve missions on CheckiO
   and how to get the most out of solving them. When the mission is solved, one more station become
   available for you, containing more complex missions.
        So this mission is the easiest one. Write a function that will receive 2 numbers as input and
   it should return the multiplication of these 2 numbers.

   Input: Two arguments. Both are int
   Output: Int
"""


def mult_two(a, b):
    return a * b  # Just return product of two number


if __name__ == '__main__':
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
