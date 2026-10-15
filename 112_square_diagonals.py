"""Problem 112: Square Diagonals."""

n = int(input("Odd size recommended: "))
for i in range(n):
    print("".join("*" if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or i+j == n-1 else " " for j in range(n)))
