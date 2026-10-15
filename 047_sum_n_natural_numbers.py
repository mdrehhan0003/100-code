"""Problem 47: Sum N Natural Numbers."""

n = int(input("N: "))
print("Sum:", n*(n+1)//2 if n >= 0 else "N should be non-negative")
