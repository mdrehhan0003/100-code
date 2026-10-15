"""Problem 106: Zigzag Pattern."""

n = int(input("Number of rows: "))
for i in range(n):
    print("*"*(n if i % 2 == 0 else 1))
