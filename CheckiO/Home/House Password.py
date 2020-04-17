"""
In this mission you should check if all elements in the given list are equal.

Input: List.
Output: Bool.
"""


def checkio(data: str) -> bool:
    if len(data) >= 10:
        for i in data:
            if i.isdigit():
                for j in data:
                    if j.isupper():
                        for k in data:
                            if k.islower():
                                return True

    return False


if __name__ == '__main__':

    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
