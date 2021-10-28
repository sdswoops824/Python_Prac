def rec_sum(n):
     s = 0.0
     for i in range (1,n+1):
          s = s + 1.0/(i)

     return(s)

for i in range (12000, 15000):
     x = 0.0
     x = rec_sum(i)
     if x > 10:
          print(i)

print(rec_sum(15000))

# 1835421