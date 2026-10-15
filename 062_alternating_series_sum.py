"""Problem 62: Alternating Series Sum."""

n = int(input("N: "))
print("Sum:", sum(i if i % 2 else -i for i in range(1, n+1)))
