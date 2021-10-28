def po(n):
    range = []
    for i in range(1, n):
        if (1234567890 % i) == 0:
           range.append(i)
    return sum(range)

# print(po(30000000))

def sum_div(number):
    divisors = []
    for i in range(1, number-1):
        if (1234567890 % i)==0:
            divisors.append(i)
    return sum(divisors)

print(sum_div(30000000))
