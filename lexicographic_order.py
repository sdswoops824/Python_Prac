from itertools import permutations

def lexicographic_perm(str):
    perm = sorted(''.join(chars) for chars in permutations(str))
    print(perm.index(str) + 1,'/',len(perm))
    for x in perm:
        print(x)

str = 'abbczi'
lexicographic_perm(str)
