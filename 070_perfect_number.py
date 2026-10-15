"""Problem 70: Perfect Number."""

n = int(input("Positive integer: "))
total = sum(i for i in range(1, n) if n > 0 and n % i == 0)
print("Perfect number" if n > 0 and total == n else "Not a perfect number")
