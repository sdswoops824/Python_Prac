# Imagine you have 30 stamps of 205¥, 40 stamps of 82¥, and 30 stamps of 30¥.
#
# Find how many values can be formed by using any combination of at least one of those stamps.
#


s1 = 205
n1 = 30

s2 = 82
n2 = 40

s3 = 30
n3 = 30

count = 0
store = []

for i in range(1, 30):
    for k in range(1, 40):
        for l in range(1, 30):
            sum = (i*205)+(k*82)+(l*30)
            # print (sum)
            if sum not in store:
                count = count + 1
                store.append(sum)

print(count)