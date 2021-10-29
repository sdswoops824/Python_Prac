# count th prime numbers below a number

def getprimecount(n):
    count = 0

    for i in range (2, n+1):
        count_f = 0
        for k in range (2, (i//2)+1):
            if i % k == 0:
                prime = False
                count_f = count_f + 1

        if count_f == 0:
            prime = True
            count = count + 1

    return count

print(getprimecount(1000))