import math


def sevenish_number(number):
    _sum = 0
    while number > 0:
        power = int(math.log(number, 2))
        number = number - 2 ** power
        _sum += 7 ** power
    return _sum


print(sevenish_number(7))
