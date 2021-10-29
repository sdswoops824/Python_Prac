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

def digits_sum(n):
    digits = [int(x) for x in str(n)]
    return sum(digits)

def reverse(n):
    rev_digits = []
    digits = [int(x) for x in str(n)]
    for i in range(len(digits)-1,0-1,-1):
        rev_digits.append(digits[i])
    strings = [str(c) for c in rev_digits]
    a_string = "".join(strings)
    return int(a_string)


print(reverse(2346765))