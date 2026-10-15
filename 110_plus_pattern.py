"""Problem 110: Plus Pattern."""

n = int(input("Odd size recommended: "))
mid = n//2
for i in range(n):
    print("".join("*" if i == mid or j == mid else " " for j in range(n)))
