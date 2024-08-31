import math


def square(side):
    s = side * side
    # округление результата
    return math.ceil(s)


print(square(3))
print(square(2.5))
