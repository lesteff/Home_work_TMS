import math


x = 0.5
n_terms = 10

cos_approx = sum((-1)**n * x**(2*n)/math.factorial(2*n) for n in range(n_terms))

print(f"Приближение: {cos_approx:.10f}")
print(f"Точное значение: {math.cos(x):.10f}")
print(f"Разница: {abs(math.cos(x) - cos_approx):.2e}")