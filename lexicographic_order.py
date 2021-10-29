from itertools import permutations

def lexicographic_perm(str):
    perm = sorted(''.join(chars) for chars in permutations(str))
    print(perm.index(str))
    for x in perm:
        print(x)

str = 'cba'
lexicographic_perm(str)
