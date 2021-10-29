def count_digits(n):
    count = 1
    rem = 1

    while rem != 0:
        rem = n // (pow(10,count))
        count = count + 1

    return count-1

def count_digits_easy(n):
    digits = [int(x) for x in str(n)]
    return len(digits)


print(count_digits_easy(2346765))