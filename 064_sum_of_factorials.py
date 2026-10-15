"""Problem 64: Sum Of Factorials."""

n = int(input("N: "))
factorial = total = 1
total = 0
for i in range(1, n+1):
    factorial *= i
    total += factorial
print("Sum of factorials:", total)
