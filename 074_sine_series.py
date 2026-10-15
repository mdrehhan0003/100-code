"""Problem 74: Sine Series."""

import math
x = float(input("x: "))
n = int(input("Number of terms: "))
total = 0.0
for k in range(n):
    power = 2*k + 1
    term = x**power / math.factorial(power)
    total += term if k % 2 == 0 else -term
print("Approximate sin(x):", total)
