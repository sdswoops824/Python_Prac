# Let's define an "A type" number as an integer that follows one or more of the conditions listed below.

# Is a mutiple of 3.
# Has a "3" in its representation, if written using the decimal system.
# E.g. 9, 31, 42, 135 are all "A type" numbers.


# Find the sum of all "A type" numbers between 1 and 50000.

divisors = []

for i in range (1, 10):
    digits = [int(x) for x in str(i)]
    if (i % 3) == 0 or 3 in digits:
        divisors.append(i)

print(sum(divisors))