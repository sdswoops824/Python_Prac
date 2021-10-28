# Python3 Program to
# find the sum of
# forth powers of
# first n natural numbers
# Return the sum of
# forth power of
# first n natural
# numbers

import math

def fourthPowerSum(n):
    return ((6 * n * n * n * n * n) +
            (15 * n * n * n * n) +
            (10 * n * n * n) - n) / 30


# Driver method
n = 80
print(fourthPowerSum(n))