"""Problem 109: X Pattern."""

n = int(input("Odd size for X: "))
for i in range(n):
    print("".join("*" if j == i or j == n-1-i else " " for j in range(n)))
