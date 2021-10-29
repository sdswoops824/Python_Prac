# count th prime numbers below a number

def getprimecount(n):
    count = 0

    for i in range (2, n+1):
        if ifprime(i) == True:
            count = count + 1

    return count

def ifprime(num):
    prime = True
    for k in range(2, (num // 2) + 1):
        if num % k == 0:
            prime = False
    return prime

print(ifprime(20))

print(getprimecount(10000))