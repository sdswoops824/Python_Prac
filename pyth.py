# python program to find the number of
# right triangles with given perimeter

# no triangle if p is odd
# if p % 2 != 0:
#     return 0
# else:
#     count = 0
#     for b in range(1, p // 2):
#
#         a = p / 2 * ((p - 2 * b) / (p - b))
#         inta = int(a)
#         if (a == inta):
#
#             # make (a, b) pair in sorted order
#             ab = tuple(sorted((inta, b)))
#
#             # check to avoid duplicates
#             if ab not in store:
#                 count += 1
#                 # store the new pair
#                 store.append(ab)

# Function to return the count
import math


def countTriangles(n):
    # making a list to store (a, b) pairs
    store = []
    count = 0
    for a in range (1, n):
        for b in range (1, n):
            if a * b < n:
                p = math.sqrt((a*a)+(b*b))
                if (p).is_integer() == True:
                    aint = int(a)
                    bint = int(b)
                    ab = tuple(sorted((aint,bint)))
                    if ab not in store:
                        count += 1
                        store.append(ab)

    return count


# Driver Code
print(countTriangles(20000))