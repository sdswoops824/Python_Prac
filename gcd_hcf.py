def gcdof(x, y):
    gcd = 0

    while(x!=y):
        if(x>y):
            x=x-y
        else:
            y=y-x
    gcd = y
    return gcd


def hcfof(x, y):
    hcf = 0
    return hcf

print(gcdof(5,15))