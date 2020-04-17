"""
Input: Time in a 24-hour format (as a string).
Output: Time in a 12-hour format (as a string).
"""


def time_converter(time):
    hour, minutes = time.split(":")
    hour = int(hour)
    if 0 < hour < 12:
        return f"{hour}:{minutes} a.m."
    elif hour == 0:
        return f"{hour + 12}:{minutes} a.m."
    elif hour == 12:
        return f"{hour}:{minutes} p.m."

    return f"{hour - 12}:{minutes} p.m."


if __name__ == '__main__':
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
