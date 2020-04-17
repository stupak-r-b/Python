"""
A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).
Output: "X", "O" or "D" as a string.
"""
from typing import List


def checkio(game_result: List[str]) -> str:
    lis = "".join(i for i in game_result)

    # win options
    win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
           [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]]

    while True:
        for i in win:
            a, b, c = lis[i[0]], lis[i[1]], lis[i[2]]
            if a + b + c == "XXX":
                return "X"
            elif a + b + c == "OOO":
                return "O"
        return "D"


if __name__ == '__main__':

    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
