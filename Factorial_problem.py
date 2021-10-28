# Prime factors of 2 and 5 produce trailing zeros
# number of 2s will always be greater than the number of 5s
# Just calculate the number of 5s

def trailingzeros(n):
    count = 0
    origin = n

    while origin != 0:

        this = origin
        while this % 5 == 0:
            count = count + 1
            this = this // 5

        origin = origin - 1

    return count

print(trailingzeros(150))