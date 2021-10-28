def TribRec(n) :
    if (n == 0 or n == 1 or n == 2) :
        return []
    elif (n == 3) :
        return [0,1][:n]
    else :
        sequence = TribRec(n-1)
        sequence.append(sequence[len(sequence)-1] +
        sequence[len(sequence)-2] + sequence[len(sequence)-3])
        return sequence


def Trib(n) :
    for i in range(1, n) :
        print( TribRec(i) , " ", end = "")

# Driver code
n = 10
Trib(n)



def tri(n):
    x = 1
    y = 0
    z = 5
    for i in range(1, n):
        x4 = x + y + z
        x = y
        y = z
        z = x4

    return(x4)

print(tri(26))