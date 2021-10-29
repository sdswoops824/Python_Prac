import math


def squareroot(num):
    if num < 2:
        return num

    x0 = num
    x1 = (x0 + num / x0) / 2.0

    while abs(x0-x1) >= 1:
        x0 = x1
        x1 = (x0 + num / x0) / 2.0

    return int(x1)

print(squareroot(9))