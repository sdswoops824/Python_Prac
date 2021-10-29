def sum(n):
    sum = 0
    for i in range (1,n+1):
        sum = sum + i
    return sum

print(sum(23))

def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def inv_fact(n):
    return (1/fact(n))

def pro(x,n):
    pro = pow(x,n)/fact(n)
    return pro

print(pro(4,5))
