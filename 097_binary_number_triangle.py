"""Problem 97: Binary Number Triangle."""

n = int(input("Rows: "))
for i in range(1, n+1): print("".join(str(j % 2) for j in range(i)))
