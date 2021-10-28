def sum_div(number):
    divisors = [1]
    for i in range(2, 20000000):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)

print(sum_div(1234567890))
