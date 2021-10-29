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

def squareroot_binarysearch(num):
    sqrt = 0
    start = 1
    end = num

    while start < end:
        cur_start = start
        cur_end = end
        guess = int((start+end)/2)
        if guess*guess > num:
            end = guess
        elif guess*guess < num:
            start = guess
        elif guess*guess == num:
            sqrt = guess
            start = end
        if start == cur_start and end == cur_end:
            return guess

    return sqrt

def cuberoot_binarysearch(num):
    cbrt = 0
    start = 1
    end = num

    while start < end:
        cur_start = start
        cur_end = end
        guess = int((start+end)/2)
        if (guess*guess*guess) > num:
            end = guess
        elif (guess*guess*guess) < num:
            start = guess
        elif (guess*guess*guess) == num:
            cbrt = guess
            start = end

        if start == cur_start and end == cur_end:
            return guess

    return cbrt

print(squareroot_binarysearch(36))
print(cuberoot_binarysearch(1331))
