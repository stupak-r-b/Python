"""
You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.
Output: The number of safe pawns as a integer
"""


def safe_pawns(pawns: set) -> int:
    chess_board = [letter + str(num) for num in range(1, 9)
                   for letter in "abcdefgh"]
    count = 0
    nums = [7, 15, 23, 31, 39, 47, 55, 63, 0, 8,
            16, 24, 32, 40, 48, 56, 1, 2, 3, 4, 5, 6]

    # rools
    for i in list(pawns):
        j = chess_board.index(i)
        if j not in nums:
            if chess_board[j - 7] in pawns \
                    or chess_board[j - 9] in pawns:
                count += 1
        elif j in [7, 15, 23, 31, 39, 47, 55, 63]:
            if chess_board[j - 9] in pawns:
                count += 1
        elif j in [0, 8, 16, 24, 32, 40, 48, 56]:
            if chess_board[j - 7] in pawns:
                count += 1

    # the number of safe pawns as a integer
    return count


if __name__ == '__main__':

    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
