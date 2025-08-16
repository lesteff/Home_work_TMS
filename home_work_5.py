import math
#Первая формула
x = 1
count = 0
for n in range(10):
    term = (-1)**n * x**(2*n + 1) / math.factorial(2 * n + 1)
    count += term
print(count)

